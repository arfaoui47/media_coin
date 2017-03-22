import requests

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Profile


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user and not user.is_anonymous():
            social = user.social_auth.get(provider='facebook')
            uid = social.uid
            image = requests.get(
                "http://graph.facebook.com/{}/picture?redirect=false&type=large".format(uid)
            ).json()
            user_api_token = Profile.objects.get(user=user).token

            context = {
                'user': user,
                'request': self.request,
                'image': image['data']['url'],
                'api_token': user_api_token
            }
        else:
            context = {'request': self.request}

        return context


def login_e(request):
    return render(request, 'index.html', {'request': request, 'error': True})
