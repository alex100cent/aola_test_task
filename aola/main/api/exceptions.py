from rest_framework.exceptions import APIException


class InvalidFilterKeyword(APIException):
    status_code = 400
    default_detail = 'Received an invalid filter keyword'
    default_code = 'invalid_filter_keyword'
