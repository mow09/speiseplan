# Generated by Django 4.0.6 on 2022-07-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_alter_info_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwlImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True, verbose_name='Name')),
                ('img', models.ImageField(upload_to='', verbose_name='Bild')),
            ],
            options={'verbose_name': 'Owl-Bild', 'verbose_name_plural': 'Owl-Bilder'},
        ),
        migrations.AddField(
            model_name='news',
            name='is_important',
            field=models.BooleanField(default=False, verbose_name='Hervorheben'),
        ),
    ]
