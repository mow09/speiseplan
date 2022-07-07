import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField

from utils.fields import SelectArrayField
from food.models import Meal


class News(models.Model):
    """News for News-Page."""
    title = models.CharField('Schlagzeile', max_length=255)
    description = models.TextField(
        'Beschreibung', max_length=1023)
    date = models.DateField(
        "Erstellt am:",
        default=datetime.date.today,
        help_text="Die Nachrichten werden anhand dieses Datums chronologisch sortiert."
    )

    class Meta:
        verbose_name = "Aktuell"
        verbose_name_plural = "Aktuelles"


class Info(models.Model):
    """Info for Landing-Page/Index."""
    title = models.CharField('Schlagzeile', max_length=255)
    description = models.TextField(
        'Beschreibung', max_length=1023)
    DAYS_CHOICES = (
        ("Mo", "Montag"),
        ("Di", "Dienstag"),
        ("Mi", "Mittwoch"),
        ("Do", "Donnerstag"),
        ("Fr", "Freitag"),
        ("Sa", "Samstag"),
        ("So", "Sonntag"),
    )
    days = SelectArrayField(
        models.CharField(
            choices=DAYS_CHOICES,
            max_length=15,
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


class Place(models.Model):
    name = models.CharField('Schlagzeile', max_length=127)
    # location =
    meals = models.ManyToManyField(Meal, blank=True)

    class Meta:
        verbose_name = "Restaurant/Café"
        verbose_name_plural = "Restaurant/Café"


class Opening(models.Model):
    """Opening times."""

    place = models.ForeignKey(Place, verbose_name='Restaurant/Café', on_delete=models.CASCADE)
    times = ArrayField(
        models.CharField(
            max_length=42,
        ),
        verbose_name="Öffnunfgszeiten",
        help_text="Alle Tage mit ihren Zeiten [Di. 9:30 Uhr - 11:30 Uhr]:",
    )

    class Meta:
        verbose_name = "Öffnungszeit"
        verbose_name_plural = "Öffnungszeiten"

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
