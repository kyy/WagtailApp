import os
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from wagtail.images import get_image_model


@receiver(post_save, sender=get_image_model())
def resize_images_on_upload(sender, instance, created=False, **kwargs):
    if (instance.width and instance.height) > 2000:
        if created:
            croped_image = instance.get_rendition('max-2000x2000|jpegquality-80')
            croped_file = croped_image.file.path
            original_file = instance.file.path
            try:
                os.rename(croped_file, original_file)
            except FileExistsError:
                os.replace(croped_file, original_file)
            instance.width = croped_image.width
            instance.height = croped_image.height
            instance.file_size = os.path.getsize(original_file)
            instance.save()
            print('upload image signal')


@receiver(post_save, sender=get_image_model())
def resize_images_on_edit(sender, instance, **kwargs):
    if (instance.width and instance.height) > 2000:
        old = sender.objects.get(pk=instance.pk)
        if old.file.path == instance.file.path:
            croped_image = instance.get_rendition('max-2000x2000|jpegquality-80')
            croped_file = croped_image.file.path
            original_file = instance.file.path
            try:
                os.rename(croped_file, original_file)
            except FileExistsError:
                os.replace(croped_file, original_file)
            instance.width = croped_image.width
            instance.height = croped_image.height
            instance.file_size = os.path.getsize(original_file)
            instance.save()
            print('edit image signal')
