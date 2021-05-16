from django.db import models


class CreateUpdateModel(models.Model):
    """ An abstract class for models with created/updated information. """

    created = models.DateTimeField(
        db_index=True,
        auto_now_add=True,
        editable=False,
    )
    updated = models.DateTimeField(
        db_index=True,
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True
