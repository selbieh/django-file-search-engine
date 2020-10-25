from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.

def file_upload(instance, filename):
    return '{0}/{1}'.format(instance.title, filename)


class StoredFiles(models.Model):
    EXTENSIONS = ["ppsx", "ppt", "pptm", "pptx", "pdf", "PDF","txt"]
    title = models.CharField(blank=False, null=False ,max_length=55)
    file = models.FileField(blank=False, upload_to=file_upload,
                            validators=[FileExtensionValidator(EXTENSIONS)])

    def __str__(self):
        return self.title
