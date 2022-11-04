# Generated by Django 4.1.2 on 2022-11-04 14:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("games", "0001_initial"),
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Championship",
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
                ("description", models.TextField()),
                ("initial_date", models.DateField()),
                ("end_date", models.DateField()),
                ("award", models.FloatField()),
                (
                    "games",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="championship",
                        to="games.game",
                    ),
                ),
                (
                    "teams",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="championship",
                        to="teams.team",
                    ),
                ),
            ],
        ),
    ]