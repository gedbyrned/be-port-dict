# Generated by Django 5.1 on 2024-10-07 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_resources"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resources",
            name="resource_description",
            field=models.CharField(blank=True, null=True),
        ),
    ]
