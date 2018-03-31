from django.db import models
from django.urls import reverse


class Post(models.Model):

    post_title = models.CharField(max_length=50)
    post_content = models.CharField(max_length=1000)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('my_blog:detail', kwargs={'pk': self.pk})
