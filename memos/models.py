from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Memo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)