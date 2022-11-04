from rest_framework import serializers
from datetime import date

from teams.models import Team
from players.models import Player
from stadiums.models import Stadium
from championships.models import Championship


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium

        fields = [
            "id",
            "name",
            "description",
            "capacity",
            "localizations",
            "area",
        ]


class PlayerSerializer(serializers.ModelSerializer):
    number_of_goals = serializers.IntegerField(min_value=0)

    class Meta:
        model = Player

        fields = (
            "id",
            "name",
            "birthdate",
            "hometown",
            "number_of_goals",
            "position",
            "shirt_number",
        )


class TeamSerializer(serializers.ModelSerializer):
    stadium = StadiumSerializer(read_only=True)
    players = PlayerSerializer(many=True, read_only=True)
    number_of_players = serializers.SerializerMethodField()

    class Meta:
        model = Team

        fields = (
            "id",
            "name",
            "mascot",
            "number_of_players",
            "team_foundation_year",
            "updated_at",
            "stadium",
            "players",
        )

    def get_number_of_players(self, obj: Team) -> int:
        return obj.players.all().count()


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model: Championship

        fields = (
            "id",
            "name",
            "description",
            "initial_date",
            "end_date",
            "award",
        )