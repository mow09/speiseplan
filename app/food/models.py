from django.db import models, IntegrityError, transaction
from utils.fields import SelectArrayField
from django.utils.crypto import get_random_string

# from content.models import Place
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete
from PIL import Image

from content.utils import germanslugify


def rand_chars(length=4):
    return get_random_string(length=length)


class Allergy(models.Model):
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=511)

    class Meta:
        verbose_name = "Allergie"
        verbose_name_plural = "Allergien"

    def __str__(self):
        return self.name


class Additive(models.Model):
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=511)

    class Meta:
        verbose_name = "Zusatzstoff"
        verbose_name_plural = "Zusatzstoffe"

    def __str__(self):
        return self.name


class Category(models.Model):
    """Meal Category."""
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=511, blank=True, null=True)
    slug = models.CharField(max_length=142, blank=True, unique=True, editable=False)

    class Meta:
        verbose_name = "Essenskategorie"
        verbose_name_plural = "Essenskategorien"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = germanslugify(self.name)
        while True:
            try:
                with transaction.atomic():
                    return super(Category, self).save(*args, **kwargs)
            except IntegrityError as e:
                # except IntegrityError or transaction.TransactionManagementError as e:
                self.slug = germanslugify(self.name+'-'+rand_chars())


class Region(models.Model):
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=511)
    # location

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regionen"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=511, blank=True, null=True)
    # additives = models.ManyToManyField(Additive, blank=True)
    # region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Zutat"
        verbose_name_plural = "Zutaten"

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField('Name', max_length=63, unique=True)
    description = models.TextField('Beschreibung', max_length=127)
    description_long = models.TextField('Beschreibung', blank=True, max_length=1023)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField('Preis in Euro', max_digits=5, decimal_places=2)
    # place = models.ForeignKey('content.Place', on_delete=models.PROTECT)
    img = models.ImageField('Bild', upload_to='meal-images', default='meal-images/berries.jpg')

    show = models.BooleanField('Ist vorhanden:', default=True,)
    special_offer = models.BooleanField(default=False)

    ingredients = models.ManyToManyField(Ingredient, blank=True, verbose_name='Zutaten')
    additives = models.ManyToManyField(Additive, blank=True, verbose_name='Zusatzstoffe')
    allergies = models.ManyToManyField(Allergy, blank=True, verbose_name='Allergiehinweise')

    bio = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False, verbose_name='vegan')
    vegetarian = models.BooleanField(default=False, verbose_name='vegetarisch')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)
    MONTH_CHOICES = (
        ('1', 'Januar'),
        ('2', 'Februar'),
        ('3', 'März'),
        ('4', 'April'),
        ('5', 'Mai'),
        ('6', 'Juni'),
        ('7', 'Juli'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'Oktober'),
        ('11', 'November'),
        ('12', 'Dezember'),
    )
    saisonal_month = SelectArrayField(
        models.CharField(
            max_length=2,
            choices=MONTH_CHOICES,
            blank=True,
            null=True
        ),
        verbose_name="Saisonale Monate",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Speise"
        verbose_name_plural = "Speisen"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # when vegan -> also vegetarian
        super().save(*args, **kwargs)

        img = Image.open(self.img.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.img.path)


@receiver(pre_delete, sender=Meal)
def owlimage_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.img.delete(False)
