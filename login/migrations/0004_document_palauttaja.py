# Generated by Django 2.0.2 on 2018-03-20 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0003_remove_document_palauttaja'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='palauttaja',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]