from django.db import models
from users.models import Civil_User, Soldier_User

# Create your models here.
class Letter(models.Model):
    img = models.ImageField(blank=True, null=True, upload_to="blog/%Y/%m/%d")
    title = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(max_length=1000, blank=True, null=True)
    civil_user = models.ForeignKey(Civil_User, on_delete=models.CASCADE, blank=True)
    soldier_user = models.ForeignKey(Soldier_User, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ': ' + self.comment[:3]