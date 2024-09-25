# automatically generated with ChatGPT

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_four_digit_number(value):
    if not str(value).isdigit() or len(str(value)) != 4:
        raise ValidationError(
            _('Value must be a four digit number.'),
            code='invalid_four_digit_number'
        )