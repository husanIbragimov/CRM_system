from django.db import models

from apps.team_user.models import Account
# from channels.layers import Layer


class Notification(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    notification = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print('Saved')
        super(Notification, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

