from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

    def test_user_creation(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Test User", email="user@test.com", team=team)
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.team, team)

    def test_activity_creation(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(name="Test User", email="user@test.com", team=team)
        activity = Activity.objects.create(user=user, type="Running", duration=30, calories=300)
        self.assertEqual(activity.type, "Running")
        self.assertEqual(activity.user, user)

    def test_workout_creation(self):
        user = User.objects.create(name="Test User", email="user@test.com", team=Team.objects.create(name="Test Team"))
        workout = Workout.objects.create(name="Cardio", description="Cardio workout")
        workout.suggested_for.add(user)
        self.assertIn(user, workout.suggested_for.all())

    def test_leaderboard_creation(self):
        team = Team.objects.create(name="Test Team")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team, team)
        self.assertEqual(leaderboard.points, 100)
