from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

# 1st way Extended profile
class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField(null=True)

    # ...

    class Meta:
        abstract = True


# 2nd way AbstractUser


class BlogUser(AbstractUser):
    dob = models.DateField(null=True)
    # ...


# 3rd way Proxy

# class ProxyUser(User):
#
#     @property
#     def full_name(self):
#         return self.get_full_name()
#
#     class Meta:
#         proxy = True
#         ordering = ['-id']
