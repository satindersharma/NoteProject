from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.text import Truncator
from django.db.models.signals import post_save
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(db_column='name',
                            max_length=45, blank=True)


    def __str__(self):
        if self.name is not None:
            return self.name
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = 'user'
        unique_together = ('email',)



class UserProfile(models.Model):
    id = models.SmallAutoField(primary_key=True)
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="userprofile/%Y/%m/%d/",
                            default='user-profile.png', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")
        db_table = 'user_profile'


# create the user profile is a new user created
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.create(user=instance)


# attached a post save signal to the user model
post_save.connect(create_user_profile, sender=CustomUser)