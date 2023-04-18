import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from wagtail.images import get_image_model
from django.shortcuts import get_object_or_404
from wagtailcache.cache import clear_cache
from wagtail import hooks


@receiver(post_save, sender=get_image_model())
def resize_images_on_upload_or_edit(sender, instance, **kwargs):
    """
    Resize, and change quality of images on upload and edit
    """
    if (instance.width and instance.height) > 2000 or instance.file_size > 500_000:
        if get_object_or_404(sender, pk=instance.pk):
            croped_image = instance.get_rendition('max-2000x2000|jpegquality-80')
            try:
                croped_file = croped_image.file.path
                instance.width = croped_image.width
                instance.height = croped_image.height
                instance.file_size = os.path.getsize(croped_file)
                original_file = instance.file.path
                os.remove(original_file)
                instance.save()
                try:
                    os.rename(croped_file, original_file)
                except FileExistsError:
                    os.replace(croped_file, original_file)
            except IOError:
                pass


def clear_wagtailcache(*args, **kwargs):
    clear_cache()


# Clear cache whenever pages/snippets are changed. Err on the side of clearing
# the cache vs not clearing the cache, as this usually leads to support requests
# when staff members make edits but do not see the changes.
hooks.register("after_delete_page", clear_wagtailcache)
hooks.register("after_move_page", clear_wagtailcache)
hooks.register("after_publish_page", clear_wagtailcache)
hooks.register("after_unpublish_page", clear_wagtailcache)
hooks.register("after_create_snippet", clear_wagtailcache)
hooks.register("after_edit_snippet", clear_wagtailcache)
hooks.register("after_delete_snippet", clear_wagtailcache)
