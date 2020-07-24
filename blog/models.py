from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#auto_now=True ::update the dateTime everytime the post was updated
#auto_now_add=True::set the dateTime only when the object was created, you cannot update it
# Create your models here.
class Post(models.Model):
    title =   models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
