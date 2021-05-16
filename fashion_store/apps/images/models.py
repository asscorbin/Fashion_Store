from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from fashion_store.apps.product.models import ProductPropertyModel
from utils.abstract_models import CreateUpdateModel


def validate_file_size(value):
    filesize = value.size
    if filesize > 1024 * 1024 * 1:
        raise ValidationError("The maximum file size that "
                              "can be uploaded is 1MB")
    else:
        return value


class ImageModel(CreateUpdateModel):
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True,
                              validators=[validate_file_size])
    product = models.ForeignKey(ProductPropertyModel, on_delete=models.CASCADE)


@receiver(pre_delete, sender=ImageModel)
def delete_image_in_folder(sender, instance, using, **kwargs):
    instance.image.delete()
