from django.db import models
from django.utils.translation import gettext, gettext_lazy as _
from django.urls import reverse
# Create your models here.


class Note(models.Model):
    title = models.CharField(_("Title"), max_length=64)
    content = models.CharField(_("Content"), max_length=512,blank=True)
    is_favourite = models.BooleanField(default=False)
    user = models.ForeignKey('users.CustomUser',on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['updated_at','created_at']
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")
        db_table = "note"


    def __str__(self):
        return self.title
    
    def get_detail_url(self):
        return reverse('noteapp:note-detail',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('noteapp:note-update',kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse('noteapp:note-delete',kwargs={'pk':self.pk})