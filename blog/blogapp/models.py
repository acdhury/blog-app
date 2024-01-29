from django.db import models

class Blogs(models.Model):  # Rename the model to singular form, Blog
    blog = models.TextField()

    def __str__(self):
        return self.blog

class User(models.Model):
    email = models.EmailField()
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.email