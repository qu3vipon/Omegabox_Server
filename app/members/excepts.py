from rest_framework import status
from rest_framework.exceptions import APIException


# Sign Up
class TakenEmailException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '이미 가입된 이메일 주소입니다.'
    default_code = 'TakenEmail'


class UsernameDuplicateException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '이미 가입된 아이디입니다.'
    default_code = 'DuplicatedUsername'


class PasswordNotMatchingException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'password1과 password2과 다릅니다.'
    default_code = 'PasswordNotMatching'


# Social Sign Up
class GoogleUniqueIdDuplicatesException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '동일한 unique_id(id_token)를 가진 사용자가 이미 존재합니다.'
    default_code = 'GoogleUniqueIdDuplicates'


class SocialSignUpUsernameFieldException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '소셜 회원가입시 username과 email이 동일해야합니다.'
    default_code = 'SocialSignUpUsernameField'


class LoginFailException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '로그인 실패 - username과 password를 확인해주세요.'
    default_code = 'LoginFail'


class UnidentifiedUniqueIdException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '해당 사용자의 unique_id와 일치하지 않습니다.'
    default_code = 'UnidentifiedUniqueId'
