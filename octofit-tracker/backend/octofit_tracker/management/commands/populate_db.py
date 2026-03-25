

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from pymongo import MongoClient


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboards.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index('email', unique=True)

        # Insert users
        users = [
            {"username": "ironman", "email": "ironman@marvel.com", "first_name": "Tony", "last_name": "Stark", "team": "Marvel"},
            {"username": "spiderman", "email": "spiderman@marvel.com", "first_name": "Peter", "last_name": "Parker", "team": "Marvel"},
            {"username": "batman", "email": "batman@dc.com", "first_name": "Bruce", "last_name": "Wayne", "team": "DC"},
            {"username": "superman", "email": "superman@dc.com", "first_name": "Clark", "last_name": "Kent", "team": "DC"},
        ]
        db.users.insert_many(users)

        # Insert teams
        teams = [
            {"name": "Marvel"},
            {"name": "DC"},
        ]
        db.teams.insert_many(teams)

        # Insert activities
        activities = [
            {"user": "ironman", "type": "run", "duration": 30},
            {"user": "spiderman", "type": "cycle", "duration": 45},
            {"user": "batman", "type": "swim", "duration": 60},
            {"user": "superman", "type": "run", "duration": 50},
        ]
        db.activities.insert_many(activities)

        # Insert leaderboard
        leaderboards = [
            {"team": "Marvel", "points": 75},
            {"team": "DC", "points": 110},
        ]
        db.leaderboards.insert_many(leaderboards)

        # Insert workouts
        workouts = [
            {"name": "Pushups", "difficulty": "Easy"},
            {"name": "Pullups", "difficulty": "Medium"},
            {"name": "Squats", "difficulty": "Easy"},
            {"name": "Deadlift", "difficulty": "Hard"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data using PyMongo.'))
