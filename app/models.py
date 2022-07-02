from django.db import models
from django.core.mail import send_mail
from .tasks import send_email


from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(User, related_name='comments1', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.body

    @property
    def get_post_author_email(self):
        return self.post.author.email

    @property
    def get_commenet_author(self):
        return self.owner.username

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        send_email.delay(self.get_post_author_email, self.get_commenet_author, self.body)
        super().save(force_insert, force_update, using, update_fields)


