# Generated by Django 4.0.2 on 2022-04-17 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_alter_generallink_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generallink',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='generallink',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.company'),
        ),
        migrations.AlterField(
            model_name='generallink',
            name='language',
            field=models.CharField(blank=True, choices=[('Uzbek', "O'zbek tili"), ('Russian', 'Rus tili'), ('English', 'Ingliz tili'), ('Other', 'Boshqa'), ('Several', 'Bir nechta')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generallink',
            name='tags',
            field=models.ManyToManyField(blank=True, to='core.Tag'),
        ),
    ]
