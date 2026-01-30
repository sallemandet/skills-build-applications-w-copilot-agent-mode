from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10, distance=1.5)
        self.assertEqual(str(activity), 'Test User - run')

    def test_workout_create(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', duration=20)
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=50)
        self.assertEqual(str(leaderboard), 'Test User: 50')
