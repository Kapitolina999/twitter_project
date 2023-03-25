import datetime

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.db import models

from twitter_project.settings import VALID_EMAIL
from user.validators import LenPhoneValidator, validate_first_num_phone, EmailDomainValidator


class User(AbstractUser):
    phone = models.PositiveBigIntegerField(verbose_name='Номер телефона', unique=True,
                                           help_text='Введите номер в формате 79990000000',
                                           validators=[LenPhoneValidator(11), validate_first_num_phone],
                                           error_messages=
                                           {'unique': 'A user with that username already exists.'}
                                           )
    birthday = models.DateField(verbose_name='Дата рождения', null=True)
    date_updated = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    email = models.EmailField(verbose_name='email', unique=True,
                              validators=[EmailDomainValidator(VALID_EMAIL)])

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)

    @property
    def age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    REQUIRED_FIELDS = ['phone', 'email']