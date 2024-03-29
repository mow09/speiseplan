# Generated by Django 4.0.6 on 2022-07-07 16:15

from django.db import migrations, models
import django.db.models.deletion
import utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additive',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True, verbose_name='Name')),
                ('description', models.TextField(max_length=511, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Zusatzstoff',
                'verbose_name_plural': 'Zusatzstoffe',
            },
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True, verbose_name='Name')),
                ('description', models.TextField(max_length=511, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Allergie',
                'verbose_name_plural': 'Allergien',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True, verbose_name='Name')),
                ('description', models.TextField(max_length=511, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Essenskategorie',
                'verbose_name_plural': 'Essenskategorien',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True,
                 max_length=511, null=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Zutat',
                'verbose_name_plural': 'Zutaten',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True, verbose_name='Name')),
                ('description', models.TextField(max_length=511, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regionen',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True, verbose_name='Name')),
                ('description', models.TextField(max_length=1023, verbose_name='Beschreibung')),
                ('special_offer', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preis in Euro')),
                ('bio', models.BooleanField(default=False)),
                ('vegan', models.BooleanField(default=False, verbose_name='vegan')),
                ('vegetarian', models.BooleanField(default=False, verbose_name='vegetarisch')),
                ('saisonal_month', utils.fields.SelectArrayField(base_field=models.CharField(blank=True, choices=[(1, 'Januar'), (2, 'Februar'), (3, 'März'), (4, 'April'), (5, 'Mai'), (6, 'Juni'), (7, 'Juli'), (
                    8, 'August'), (9, 'September'), (10, 'Oktober'), (11, 'November'), (12, 'Dezember')], max_length=15, null=True), blank=True, null=True, size=None, verbose_name='Saisonale Monate')),
                ('additives', models.ManyToManyField(blank=True,
                 to='food.additive', verbose_name='Zusatzstoffe')),
                ('allergies', models.ManyToManyField(blank=True,
                 to='food.allergy', verbose_name='Allergiehinweise')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='food.category')),
                ('ingredients', models.ManyToManyField(blank=True,
                 to='food.ingredient', verbose_name='Zutaten')),
                ('region', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.SET_NULL, to='food.region')),
            ],
            options={
                'verbose_name': 'Speise',
                'verbose_name_plural': 'Speisen',
            },
        ),
    ]
