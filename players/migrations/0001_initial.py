# Generated by Django 4.1.2 on 2022-11-04 13:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Player",
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
                ("birthdate", models.DateField()),
                ("hometown", models.CharField(max_length=150)),
                ("biography", models.TextField()),
                ("number_of_goals", models.IntegerField()),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("Goleiro", "Goleiro"),
                            ("Zagueiro", "Zagueiro"),
                            ("Lateral", "Lateral"),
                            ("Meia", "Meia"),
                            ("Atacante", "Atacante"),
                            ("Jogador", "Other"),
                        ],
                        default="Jogador",
                        max_length=50,
                    ),
                ),
                ("shirt_number", models.IntegerField()),
                (
                    "current_team",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="players",
                        to="teams.team",
                    ),
                ),
            ],
        ),
    ]
