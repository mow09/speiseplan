from django.db import models
from utils.fields import SelectArrayField


class Allergy(models.Model):
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=511)

    class Meta:
        verbose_name = "Allergie"
        verbose_name_plural = "Allergien"


class Additive(models.Model):
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=511)

    class Meta:
        verbose_name = "Zusatzstoff"
        verbose_name_plural = "Zusatzstoffe"


class Category(models.Model):
    """Meal Category."""
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=511)

    class Meta:
        verbose_name = "Essenskategorie"
        verbose_name_plural = "Essenskategorien"


class Region(models.Model):
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=511)
    # location

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regionen"


class Ingredient(models.Model):
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=511, blank=True, null=True)
    # additives = models.ManyToManyField(Additive, blank=True)
    # region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Zutat"
        verbose_name_plural = "Zutaten"


class Meal(models.Model):
    name = models.CharField('Name', max_length=127, unique=True)
    description = models.TextField('Beschreibung', max_length=1023)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    special_offer = models.BooleanField(default=False)
    price = models.DecimalField('Preis in Euro', max_digits=5, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    additives = models.ManyToManyField(Additive, blank=True)
    bio = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)
    MONTH_CHOICES = (
        (1, 'Januar'),
        (2, 'Februar'),
        (3, 'März'),
        (4, 'April'),
        (5, 'Mai'),
        (6, 'Juni'),
        (7, 'Juli'),
        (8, 'August'),
        (9, 'September'),
        (10, 'Oktober'),
        (11, 'November'),
        (12, 'Dezember'),
    )
    saisonal_month = SelectArrayField(
        models.CharField(
            choices=MONTH_CHOICES,
            max_length=15,
            blank=True,
            null=True
        ),
        verbose_name="Anzeigetage",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Speise"
        verbose_name_plural = "Speisen"

    # def save():
    # when vegan -> also vegetarian