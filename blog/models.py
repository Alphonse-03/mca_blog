from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from pytz import timezone
# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=30)
    slug=models.CharField(max_length=200)
    view=models.IntegerField(default=0)
    
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + "    by    " + self.author

class Comments(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timeStamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment + "   by    " + self.user.first_name
