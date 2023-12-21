from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, )
    birth_date = models.DateField(blank=True, null=True, )
    bio = models.TextField(blank=True, null=True, )
    friends = models.ManyToManyField('self', blank=True, )

    def __str__(self):
        return self.user.username
