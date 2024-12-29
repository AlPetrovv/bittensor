from django.db import models
from django.utils.text import slugify


class Subnet(models.Model):
    name = models.CharField("Name", max_length=255, unique=True)
    number = models.PositiveIntegerField("Number", auto_created=True)
    slug = models.SlugField("Slug", max_length=255, unique=True, null=True, blank=True)
    openai_model = models.CharField(
        "OpenAI Model", max_length=50, default="gpt-4o-mini"
    )
    is_active = models.BooleanField("Active", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Subnet"
        verbose_name_plural = "Subnets"

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, force_insert, force_update, using, update_fields)
