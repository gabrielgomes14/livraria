# Generated by Django 5.1.3 on 2024-12-04 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_editora_cidade_editora_email"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="foto",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
