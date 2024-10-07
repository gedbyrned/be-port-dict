# Generated by Django 5.1 on 2024-09-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_delete_dailyword"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resources",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("resource_name", models.CharField(max_length=300)),
                ("resource_type", models.CharField(max_length=100)),
                (
                    "resource_author",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "resource_description",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "resource_level",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "resource_language",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("resource_url", models.URLField(blank=True, null=True)),
                (
                    "resource_image",
                    models.ImageField(blank=True, null=True, upload_to="resources/"),
                ),
            ],
        ),
    ]
