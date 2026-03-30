from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from pymongo import MongoClient
import os

client = MongoClient('localhost', 27017)
db = client['octofit_db']

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboards': '/api/leaderboards/',
        'workouts': '/api/workouts/',
    })

@api_view(['GET'])
def users_list(request):
    users = list(db.users.find())
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def teams_list(request):
    teams = list(db.teams.find())
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def activities_list(request):
    activities = list(db.activities.find())
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def leaderboards_list(request):
    leaderboards = list(db.leaderboards.find())
    serializer = LeaderboardSerializer(leaderboards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def workouts_list(request):
    workouts = list(db.workouts.find())
    serializer = WorkoutSerializer(workouts, many=True)
    return Response(serializer.data)
