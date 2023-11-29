from django.db import models
from django.utils.translation import gettext_lazy as _


class UserModelMixin(models.Model):
    """
    Abstract base class for models that have a user as a foreign key.
    """

    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="%(class)ss"
    )

    class Meta:
        abstract = True


class TimestampedModelMixin(models.Model):
    """Timestamp mixin

    This mixin adds a timestamp to model for create and update events
    """

    created = models.DateTimeField(
        _("created at"),
        auto_now_add=True,
        help_text=_("This is the timestamp of the object creation."),
    )
    updated = models.DateTimeField(
        _("updated at"),
        auto_now=True,
        help_text=_("This is the timestamp of the object update"),
    )

    class Meta:
        ordering = ["-created"]
        abstract = True
