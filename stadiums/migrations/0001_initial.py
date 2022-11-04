# Generated by Django 4.1.2 on 2022-11-04 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stadium",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(max_length=500)),
                ("capacity", models.PositiveIntegerField()),
                ("localizations", models.CharField(max_length=255)),
                ("area", models.FloatField()),
            ],
        ),
    ]
