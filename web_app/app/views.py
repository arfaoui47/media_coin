import requests

from django.shortcuts import render
from django.views.generic import TemplateView


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

            context = {
                'user': user,
                'request': self.request,
                'image': image['data']['url']
            }
        else:
            context = {'request': self.request}

        return context


def login_e(request):
    return render(request, 'index.html', {'request': request, 'error': True})
