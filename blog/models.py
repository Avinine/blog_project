from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)   # این عنوان پسته
    content = models.TextField()               # این متن اصلیه
    created_at = models.DateTimeField(auto_now_add=True)   # این زمان ایجادشه
    
def __str__(self):
    return self.title