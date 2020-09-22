from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib import auth # UserManagerのため

from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import uuid # UUIDFieldを使うため

# Create your models here.

# django.contrib.auth.models からコピーして編集している
class User(AbstractUser):
  pass

  # id を UUID に変更
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  # 投票ポイントの実装
  votingpoint = models.IntegerField(verbose_name='voting point', default=10)
