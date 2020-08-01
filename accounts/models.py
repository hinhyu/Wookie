from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User, AbstractUser, BaseUserManager
 
# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def create_user(self, username, email, password, nickname, school, gender):
#         user = self.model(
#             username = username,
#             email = email,
#             nickname = nickname,
#             school = school,
#             gender = gender
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, username, email, password, nickname, school, gender):
#         user = self.create_user(
#             username = username,
#             email = email,
#             nickname = nickname,
#             school = school,
#             gender = gender
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using = self._db)
#         return user

class Profile(AbstractUser):
    nickname = models.TextField(max_length=10)
    school = models.TextField(max_length=20)
    # 성별은 필터로 선택할 수 있게->서치
    # GENDER_CHOICE = {
    #     (1, 'Woman'),
    #     (2, 'Man'),
    # }
    # gender = models.IntegerField(choices=GENDER_CHOICE)
    gender = models.TextField(max_length=10)