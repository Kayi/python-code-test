from django.db import models
from django.contrib.auth.models import User
from episodes.models import Episode


class AbstractReaction(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now=True)
    episode = models.ForeignKey(Episode, related_name="%(app_label)s_%(class)s_related",
                                on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True


class ImageReaction(AbstractReaction):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return 'reaction by ' + str(self.user) + ' at ' + str(self.created_at)


class TweetReaction(AbstractReaction):
    text = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return 'comment by ' + str(self.user) + ' at ' + str(self.created_at)