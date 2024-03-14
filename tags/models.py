from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class TaggedManager(models.Manager):
    """
    The main functionality of this class is a manager that get's an object that's other class like 
    Product since it does not depends on other classes .
    that's it get all the product with a give take or get a tag and get the products related to it
    """
    def get_object_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)

        query = TaggedItem.objects.select_related('tag').filter(content_type=content_type, object_id = obj_id)

        return query



class Tag(models.Model):
    lable = models.CharField(max_length=255)


    def __str__(self):
        return self.lable



class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey()

    objects = TaggedManager()

    def __str__(self) -> str:
        return self.tag.lable
    