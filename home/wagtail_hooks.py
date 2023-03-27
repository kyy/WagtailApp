import os
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from wagtail.images import get_image_model
from django.shortcuts import get_object_or_404


@receiver(post_save, sender=get_image_model())
def resize_images_on_upload_or_edit(sender, instance, **kwargs):
    if (instance.width and instance.height) > 2000 or instance.file_size > 500_000:
        try:
            if get_object_or_404(sender, pk=instance.pk):
                croped_image = instance.get_rendition('max-2000x2000|jpegquality-80')
                croped_file = croped_image.file.path
                if os.path.exists(croped_file):
                    instance.width = croped_image.width
                    instance.height = croped_image.height
                    instance.file_size = os.path.getsize(croped_file)
                    original_file = instance.file.path
                    os.remove(original_file)
                    instance.save()
                    try:
                        os.rename(croped_file, original_file)
                    except FileExistsError as e:
                        os.replace(croped_file, original_file)
                        print('home.wagtail_hooks.resize_images_on_upload_or_edit --> FileExistsError --> ', e)
        except IOError as e:
            print('home.wagtail_hooks.resize_images_on_upload_or_edit --> IOError --> ', e)





