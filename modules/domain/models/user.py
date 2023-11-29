from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=300, blank=True)
    last_name = models.CharField(_("last name"), max_length=300, blank=True)
    username = models.CharField(max_length=100, unique=True, verbose_name=_("username"))
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        db_table = "user"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username
