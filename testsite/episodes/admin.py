from django.contrib import admin
from reactions.models import TweetReaction, ImageReaction

from .models import Episode

# Allow admin to add/remove multiple reactions to one episode i.e. many to one rel. in AdminSite
class TweetAdminInline(admin.TabularInline):
    model = TweetReaction


class ImageAdminInline(admin.TabularInline):
    model = ImageReaction


class EpisodeAdmin(admin.ModelAdmin):
    inlines = [
        TweetAdminInline,
        ImageAdminInline
    ]


admin.site.register(Episode, EpisodeAdmin)
