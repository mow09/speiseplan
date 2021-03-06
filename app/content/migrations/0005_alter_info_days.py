# Generated by Django 4.0.6 on 2022-07-08 16:01

from django.db import migrations, models
import utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_info_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='days',
            field=utils.fields.SelectArrayField(base_field=models.CharField(blank=True, choices=[('0', 'Montag'), ('1', 'Dienstag'), ('2', 'Mittwoch'), ('3', 'Donnerstag'), ('4', 'Freitag'), ('5', 'Samstag'), ('6', 'Sonntag')], max_length=1, null=True), blank=True, null=True, size=None, verbose_name='Anzeigetage'),
        ),
    ]
