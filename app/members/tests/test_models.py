from django.test import TestCase
from model_bakery import baker

from test_utils.generators import gen_phonenumberfield


class MemberModelTest(TestCase):
    baker.generators.add('phonenumber_field.modelfields.PhoneNumberField', gen_phonenumberfield)

    def test_post_save_create_profile(self):
        member = baker.make('members.Member')
        self.assertIsNotNone(member.profile)
