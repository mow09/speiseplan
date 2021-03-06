# Generated by Django 4.0.6 on 2022-07-07 14:31

import datetime
import content.models

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Schlagzeile')),
                ('description', models.TextField(max_length=1023, verbose_name='Beschreibung')),
                ('days', content.models.SelectArrayField(base_field=models.CharField(blank=True, choices=[('Mo', 'Montag'), ('Di', 'Dienstag'), ('Mi', 'Mittwoch'), (
                    'Do', 'Donnerstag'), ('Fr', 'Freitag'), ('Sa', 'Samstag'), ('So', 'Sonntag')], max_length=15, null=True), blank=True, null=True, size=None, verbose_name='Anzeigetage')),
                ('prior', models.BooleanField(default=False,
                                              help_text='Priorität endet nie, wenn Enddatum nicht gesetzt...', verbose_name='Hat priorität')),
                ('end_date', models.DateField(blank=True, help_text='Wird nur beachtet, wenn "Hat priorität" aktiviert ist...',
                 null=True, verbose_name='Priorität bis Datum (Enddatum)')),
                ('start_date', models.DateField(blank=True, help_text='Wird nur beachtet, wenn "Hat priorität" aktiviert ist...',
                 null=True, verbose_name='Priorität ab Datum (Startdatum)')),
            ],
            options={
                'verbose_name': 'Information',
                'verbose_name_plural': 'Informationen',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Schlagzeile')),
                ('description', models.TextField(max_length=1023, verbose_name='Beschreibung')),
                ('date', models.DateField(default=datetime.date.today,
                 help_text='Die Nachrichten werden anhand dieses Datums chronologisch sortiert.', verbose_name='Erstellt am:')),
            ],
            options={
                'verbose_name': 'Aktuell',
                'verbose_name_plural': 'Aktuelles',
            },
        ),
    ]
