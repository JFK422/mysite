from django.db import models

class pic(models.Model):
    #The path is just the image name, because all images are in the same folder.
    title = models.CharField(max_length=140)
    body = models.TextField(null=True)
    postDate = models.DateTimeField()

    path = models.CharField(max_length=200)
    img = models.ImageField()
    date = models.DateTimeField()
    dimensions = models.CharField(max_length=60)
    latitude = models.FloatField()
    longitude = models.FloatField()
    flash = models.BooleanField()
    focalLength = models.IntegerField()
    whiteBalance = models.CharField(max_length=20)
    aperture = models.FloatField()
    exposure = models.CharField(max_length=40)
    iso = models.IntegerField()
    cameraModel = models.CharField(max_length=40)
    editedParams = models.BooleanField()
    horizontal = models.BooleanField(default=True)

    def __str__(self):
        return self.title