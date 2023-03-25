from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class LenPhoneValidator(BaseValidator):
    def clean(self, x):
        return len(str(x))


def validate_first_num_phone(value):
    if str(value)[0] != '7':
        raise ValidationError('Ensure this value starts with 7')


class EmailDomainValidator(BaseValidator):
    message = 'Недопустимый домен электронного адреса'

    def compare(self, a: str, b: list) -> bool:
        return a not in b

    def clean(self, x: str) -> str:
        return x.rsplit('@', 1)[1]
