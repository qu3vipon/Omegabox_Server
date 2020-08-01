from django.test import TestCase
from model_bakery import baker
from rest_framework.exceptions import ValidationError


class MemberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.member = baker.make('members.Member')

    def test_post_save_create_profile(self):
        member = self.member
        self.assertIsNotNone(member.profile)


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.regions = baker.make('theaters.Region', _quantity=3)
        cls.genres = baker.make('movies.Genre', _quantity=3)
        cls.region = baker.make('theaters.Region')
        cls.genre = baker.make('movies.Genre')
        cls.member = baker.make('members.Member')

    def test_limit_regions_number(self):
        profile = self.member.profile
        profile.regions.set(self.regions)
        self.assertEqual(profile.regions.count(), 3)

        self.assertRaises(ValidationError, profile.regions.add, self.region)

    def test_limit_genres_number(self):
        profile = self.member.profile
        profile.genres.set(self.genres)
        self.assertEqual(profile.genres.count(), 3)

        self.assertRaises(ValidationError, profile.genres.add, self.genre)
