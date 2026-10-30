from django.db import models
from django.utils.translation import gettext_lazy as _

class UserType(models.IntegerChoices):
    CUSTOMER = 1, _("customer")
    ADMIN = 2, _("admin")
    SUPERUSER = 3 , _("superuser")