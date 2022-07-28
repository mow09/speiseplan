# Generated by Django 4.0.6 on 2022-07-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_meal_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='description_long',
            field=models.TextField(blank=True, max_length=1023, verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='description',
            field=models.TextField(max_length=127, verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(max_length=63, unique=True, verbose_name='Name'),
        ),
    ]