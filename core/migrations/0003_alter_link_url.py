# Generated by Django 4.0.2 on 2022-03-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_link_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(help_text="Iltimos to'g\ri URL kiriting!"),
        ),
    ]
