# Generated by Django 4.1.2 on 2022-11-08 21:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("championships", "0001_initial"),
        ("stadiums", "0001_initial"),
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Game",
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
                ("date", models.DateTimeField()),
                ("result", models.CharField(max_length=150)),
                (
                    "championship",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="games",
                        to="championships.championship",
                    ),
                ),
                (
                    "stadium",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="games",
                        to="stadiums.stadium",
                    ),
                ),
                (
                    "teams",
                    models.ManyToManyField(related_name="games", to="teams.team"),
                ),
            ],
        ),
    ]
