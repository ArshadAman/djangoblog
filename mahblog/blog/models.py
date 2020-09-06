from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# class Article(models.Model):
#     title = models.CharField(max_length=100)
#     content = EditorJSField()



class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=RichTextUploadingField(blank=True)
    author=models.CharField(max_length=100)
    suggest=models.CharField(max_length=200,default='None')
    slug=models.CharField(max_length=100, default='')
    views=models.IntegerField(default=0, editable=False)
    category=models.CharField(max_length=255, default='None')
    timeStamp=models.DateTimeField(blank=True)
    


    def __str__(self):
        return self.title+' by '+self.author


class BlogComment(models.Model):
        sno=models.AutoField(primary_key=True)
        comment=models.TextField()
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        post=models.ForeignKey(Post,on_delete=models.CASCADE)
        parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True)
        timeStamp=models.DateTimeField(default=now)
    
        def __str__(self):
            return 'Comment from '+ self.user.username +' ( '+ self.comment[0:10]+' )'

