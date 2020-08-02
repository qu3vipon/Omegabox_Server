from model_bakery import baker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from members.exceptions import (
    UsernameDuplicateException, PasswordNotMatchingException,
    GoogleUniqueIdDuplicatesException, SocialSignUpUsernameFieldException
)


class SignUpViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('members:signup')
        cls.member = baker.make('members.Member')

    def test_invalid_email(self):
        invalid_email = "INVALID-EMAIL"
        user_data = {
            "username": "username",
            "email": invalid_email,
            "name": "name",
            "mobile": "010-2222-3333",
            "birth_date": "2020-02-02",
            "password1": "testpassword123!",
            "password2": "testpassword123!",
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0].code, 'invalid')

    def test_duplicate_username(self):
        duplicate_username = self.member.username
        user_data = {
            "username": duplicate_username,
            "email": "email@email.com",
            "name": "name",
            "mobile": "010-2222-3333",
            "birth_date": "2020-02-02",
            "password1": "testpassword123!",
            "password2": "testpassword123!",
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'].code, UsernameDuplicateException.default_code)

    def test_not_matching_password1_password2(self):
        password1 = "TESTPASSWORD1"
        password2 = "TESTPASSWORD2"
        user_data = {
            "username": "username",
            "email": "email@email.com",
            "name": "name",
            "mobile": "010-2222-3333",
            "birth_date": "2020-02-02",
            "password1": password1,
            "password2": password2,
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'].code, PasswordNotMatchingException.default_code)

    def test_create_member(self):
        user_data = {
            "username": "username",
            "email": "email@email.com",
            "name": "name",
            "mobile": "010-2222-3333",
            "birth_date": "2020-02-02",
            "password1": "testpassword123!",
            "password2": "testpassword123!",
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


class SocialSignUpViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('members:social_signup')
        cls.member = baker.make('members.Member', unique_id='UNIQUE_ID')

    def test_duplicate_google_unique_id(self):
        duplicate_unique_id = self.member.unique_id
        user_data = {
            "username": "email@email.com",
            "email": "email@email.com",
            "name": "name",
            "mobile": "010-2222-3333",
            "birth_date": "2020-02-02",
            "unique_id": duplicate_unique_id,
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'].code, GoogleUniqueIdDuplicatesException.default_code)

    def test_email_as_username(self):
        user_data = {
            "username": "ThisIsNotEmail",
            "email": "email@email.com",
            "name": "name",
            "mobile": "010-2222-3333",
            "birth_date": "2020-02-02",
            "unique_id": "google_unique_id",
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'].code, SocialSignUpUsernameFieldException.default_code)

    def test_create_member(self):
        user_data = {
            "username": "email@email.com",
            "email": "email@email.com",
            "name": "name",
            "mobile": "010-2222-3333",
            "birth_date": "2020-02-02",
            "unique_id": "google_unique_id",
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
