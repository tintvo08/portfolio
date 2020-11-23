from django.db import models

# Create your models here.
# Create blog models
# Add blog app to settings
# create a migration
# migrate
# add to admin


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
