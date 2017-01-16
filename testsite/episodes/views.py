from django.shortcuts import render, HttpResponseRedirect
from django.views import generic, View
from .models import Episode
from reactions.forms import ImageReactionFormModel, TweetReactionFormModel
# Create your views here.


class Episodes(View):

    def get(self, request, episode_number=None):
        # If no id is specified, we display all episodes in list format
        if not episode_number:
            episodes = Episode.objects.all()
            return render(request, 'homepage.html', {'episodes': episodes})
        # specific episode is request
        else:
            episodes = Episode.objects.filter(episode_number=episode_number).first()
            image_form = ImageReactionFormModel
            tweet_form = TweetReactionFormModel
            return render(request, 'reactions.html', {'episodes': episodes,
                                                      'image_form': image_form,
                                                      'tweet_form': tweet_form,
                                                      'episode_number': episode_number})

    def post(self, request):
        image = ImageReactionFormModel(request.POST, request.FILES)
        comment = TweetReactionFormModel(request.POST)
        episode_number = request.POST.get('episode_number')

        if not image.is_valid() and not comment.is_valid(): # Both invalid so print errors out
            return render(request, 'reactions.html', {'image_form': image,
                                                      'tweet_form': comment,
                                                      'episode_number': episode_number
                                                      })
        # episode_id is passed as a hiddeninput, so assign it then save it!
        elif image.is_valid():
            i = image.save(commit=False)
            i.episode_id = episode_number
            i.save()
        elif comment.is_valid():
            c = comment.save(commit=False)
            c.episode_id = episode_number
            c.save()
        else:
            print('unexpected case entered')

        return HttpResponseRedirect('episode/%i' %int(episode_number))
