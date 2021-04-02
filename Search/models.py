from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SearchModel(models.Model):
    search_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_user')
    keyword = models.TextField()
    search_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-search_date',]
    def __str__(self):
        return f'{self.keyword} [{self.search_date}]'
  