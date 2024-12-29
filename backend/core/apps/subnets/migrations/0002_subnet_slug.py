# Generated by Django 5.1 on 2024-09-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subnets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subnet",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=255, null=True, unique=True, verbose_name="Slug"
            ),
        ),
    ]
