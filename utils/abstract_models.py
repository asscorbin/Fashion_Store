from django.db import models


class CreateUpdateModel(models.Model):
    """ An abstract class for models with created/updated information. """

    created = models.DateTimeField(
        db_index=True,
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True
    )
    updated = models.DateTimeField(
        db_index=True,
        auto_now=True,
        editable=False,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True
