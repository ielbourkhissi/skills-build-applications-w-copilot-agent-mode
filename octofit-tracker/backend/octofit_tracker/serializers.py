from rest_framework import serializers
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value) if isinstance(value, ObjectId) else value
    def to_internal_value(self, data):
        return ObjectId(data) if data else None

class TeamSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    name = serializers.CharField(max_length=100)

class ActivitySerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    user = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    team = serializers.CharField(max_length=100)
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    name = serializers.CharField(max_length=100)
    difficulty = serializers.CharField(max_length=50)

class UserSerializer(serializers.Serializer):
    id = ObjectIdField(read_only=True)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    team = serializers.CharField(max_length=100)
