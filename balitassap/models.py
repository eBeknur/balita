from django.db.models import CASCADE
from django.db import models
from django.db.models import TextField



class Category(models.Model):
    name = models.CharField(max_length=20 , blank=True , null=True )

    def __str__(self):
        return self.name

    def posts_count(self):
        return self.post.count()

class Tags(models.Model):
    name = models.CharField(max_length=20 , blank=True , null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30 , )
    description = models.TextField()
    main_image = models.ImageField(upload_to='media/mainimages')
    category = models.ForeignKey(Category , on_delete=models.CASCADE, null=True, blank=True , related_name='post')
    upload_to = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    tag = models.ForeignKey(Tags , on_delete=CASCADE , null=True , blank=True)
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    def comment_count(self):
        return self.post.count()

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.TextField()
    message = models.TextField()
    post = models.ForeignKey(Post , on_delete=models.CASCADE , blank=True , null=True , related_name='post')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField()
    message = models.TextField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField()
    message = models.TextField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
