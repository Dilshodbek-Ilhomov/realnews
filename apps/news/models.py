from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

# Category Model
class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

# News Model
class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title