from django.db import models


class Posts(models.Model):
    title = models.CharField(blank=True, max_length=100, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
