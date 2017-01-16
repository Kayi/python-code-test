from django.db import models


class Episode(models.Model):
    class Meta:
        # Display according to chronological order
        ordering = ['created_at']

    title = models.TextField(blank=False, null=False)
    episode_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    hero_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

