# Generated by Django 3.2 on 2022-05-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_section_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='generallink',
            name='tools',
            field=models.ManyToManyField(blank=True, null=True, to='core.GeneralLink'),
        ),
    ]
