# Generated by Django 5.1 on 2024-10-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subnets", "0002_subnet_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="subnet",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Active"),
        ),
        migrations.AddField(
            model_name="subnet",
            name="openai_model",
            field=models.CharField(
                default="gpt-4o-mini", max_length=50, verbose_name="OpenAI Model"
            ),
        ),
    ]
