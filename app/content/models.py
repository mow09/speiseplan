from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete
from datetime import date

from django.db import models, IntegrityError, transaction

# from django.contrib.postgres.fields import ArrayField
from django_jsonform.models.fields import ArrayField
from PIL import Image

# from django_better_admin_arrayfield.models.fields import ArrayField
from utils.fields import SelectArrayField
from food.models import Meal


from content.utils import germanslugify


class News(models.Model):
    """News for News-Page."""
    title = models.CharField('Schlagzeile', max_length=255,
                             help_text="Überschrift für die Titleseite.")
    description = models.TextField(
        'Mitteilung', max_length=1023)
    date = models.DateField(
        "Erstellt am:",
        default=date.today,
        help_text="Die Nachrichten werden anhand dieses Datums chronologisch sortiert."
    )
    is_important = models.BooleanField('Hervorheben', default=False)

    class Meta:
        verbose_name = "Aktuell"
        verbose_name_plural = "Aktuelles"

    def __str__(self):
        return self.title


class Info(models.Model):
    """Info for Landing-Page/Index."""
    header = models.CharField('Kopfzeile', blank=True, null=True, max_length=255)
    title = models.CharField('Schlagzeile', max_length=255)
    description = models.TextField(
        'Information', max_length=1023)
    WEEKDAY_CHOICES = (
        ("0", "Montag"),
        ("1", "Dienstag"),
        ("2", "Mittwoch"),
        ("3", "Donnerstag"),
        ("4", "Freitag"),
        ("5", "Samstag"),
        ("6", "Sonntag"),
    )
    days = SelectArrayField(
        models.CharField(
            max_length=1,
            choices=WEEKDAY_CHOICES,
            blank=True,
            null=True
        ),
        verbose_name="Anzeigetage",
        blank=True,
        null=True,
    )
    prior = models.BooleanField(
        'Hat priorität', default=False,
        help_text="Priorität endet nie, wenn Enddatum nicht gesetzt..."
    )
    start_date = models.DateField(
        'Priorität ab Datum (Startdatum)', blank=True, null=True,
        help_text='Wird nur beachtet, wenn "Hat priorität" aktiviert ist...',
    )
    end_date = models.DateField(
        'Priorität bis Datum (Enddatum)', blank=True, null=True,
        help_text='Wird nur beachtet, wenn "Hat priorität" aktiviert ist...',
    )

    class Meta:
        verbose_name = "Information"
        verbose_name_plural = "Informationen"

    def __str__(self):
        return self.title

    @classmethod
    def get_index_info(cls):
        # TODO HANDLE more prior
        # - no date
        # - just start_date
        # -just end_date
        prior_infos = cls.objects.filter(prior=True, end_date__gte=date.today())
        if not prior_infos:
            general_infos = cls.objects.filter(prior=False)

            for each in general_infos:
                print(each)

            print(general_infos)
            return general_infos.first()
        elif len(prior_infos) == 1:
            return prior_infos.first()
        else:
            # TODO handle most prior...
            return prior_infos.first()


class Place(models.Model):
    name = models.CharField('Name', max_length=127)
    # location =
    meals = models.ManyToManyField(Meal, blank=True, related_name='place')
    about = models.TextField('Über uns', blank=True)
    slug = models.CharField(max_length=142, blank=True, unique=True, editable=False)
    # img = models.ImageField(blank=True, null=True)
    # icon = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = "Restaurant/Café"
        verbose_name_plural = "Restaurant/Café"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = germanslugify(self.name)
        while True:
            try:
                with transaction.atomic():
                    return super(Place, self).save(*args, **kwargs)
            except IntegrityError as e:
                # except IntegrityError or transaction.TransactionManagementError as e:
                self.slug = germanslugify(self.name+'-'+rand_chars())


class Opening(models.Model):
    """Opening times."""

    place = models.ForeignKey(Place, verbose_name='Restaurant/Café', on_delete=models.CASCADE)

    times = ArrayField(
        models.CharField(max_length=42),
        size=10,
        verbose_name="Öffnunfgszeiten",
        help_text="Alle Tage mit ihren Zeiten [Di. 9:30 Uhr - 11:30 Uhr]:",
    )

    # times = ArrayField(
    #     models.CharField(
    #         max_length=42,
    #     ),
    #     size=8,
    #     verbose_name="Öffnunfgszeiten",
    #     help_text="Alle Tage mit ihren Zeiten [Di. 9:30 Uhr - 11:30 Uhr]:",
    # )

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"

    def __str__(self):
        return self.place.name

    # def save():
    # if prior set - > save default datetime for today


# class Page(models.Model):
#     """General page-info."""
#
#     name = models.CharField('Seitenname', max_length=255)
#     title = models.CharField('Seitentitle', max_length=255)
#
#     class Meta:
#         verbose_name = "Internetseite"
#         verbose_name_plural = "Internetseiten"

class Intro(models.Model):
    header = models.CharField('Kopfzeile', blank=True, null=True, max_length=255)
    title = models.CharField('Schlagzeile', max_length=255)
    description_list = ArrayField(
        models.TextField('Text', max_length=1023),
        size=10,
        verbose_name="Texte",
        help_text="Jede Spalte der Liste wird in einen neuen Absatz im Intro geschreiben.",
    )
    url_path = models.CharField('URL Pfad', max_length=32)

    class Meta:
        verbose_name = "Into Text"
        verbose_name_plural = "Intro Texte"

    def __str__(self, force_insert=False, force_update=False, using=None):
        return self.title + ' in ' + self.url_path

    @classmethod
    def get_intro(cls, url):
        return cls.objects.get(url_path=url)

# class Layer3(models.Model):
#     """Fix layer over footer or somewhere."""


class OwlImage(models.Model):
    name = models.CharField('Name', max_length=127, unique=True)
    img = models.ImageField('Bild', unique=True, upload_to='owl-images')

    class Meta:
        verbose_name = "Owl-Bild"
        verbose_name_plural = "Owl-Bilder"

    def __str__(self, force_insert=False, force_update=False, using=None):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.img.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.img.path)


@receiver(pre_delete, sender=OwlImage)
def owlimage_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.img.delete(False)
