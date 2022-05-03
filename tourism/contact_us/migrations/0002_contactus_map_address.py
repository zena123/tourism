# Generated by Django 3.2.13 on 2022-05-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='map_address',
            field=models.CharField(blank=True, default='', help_text='Input google map address', max_length=255, verbose_name='Map address'),
        ),
    ]
