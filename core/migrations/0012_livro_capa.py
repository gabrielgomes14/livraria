# Generated by Django 5.1.3 on 2024-12-02 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_alter_autor_options"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="capa",
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