from model_bakery import baker

from test_utils.generators import gen_phonenumber

baker.generators.add('phonenumber_field.modelfields.PhoneNumberField', gen_phonenumber)
