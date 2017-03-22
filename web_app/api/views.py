from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Time, Extension
from .utils import token_validation


@method_decorator(csrf_exempt, name='dispatch')
class UserData(View):

    @method_decorator(token_validation)
    def get(self, *args, **kwargs):
        fct = self.request.GET.get('fct', None)
        user = args[1]
        if fct == "get_data":
            response = self.get_data(user)
        elif fct == "update_data":
            response = self.update_data(user)
        elif fct is None:
            response = {
                "status": "failed",
                "error": "please specify usage function"
            }
        else:
            response = {
                "status": "failed",
                "error": "please check your fct param"
            }

        return JsonResponse(response)

    def get_data(self, user):
        try:
            data = Time.objects.get(user=user)
            time = data.time
        except:
            time = None

        response = {
            "status": "success",
            "data": {
                "time": time
            }
        }
        return response

    def update_data(self, user):
        try:
            used_time = int(self.request.GET.get('time', None))
        except:
            used_time = None

        if used_time is None:
            response = {
                "status": "failed",
                "error": "please provide valid used time"
            }
        else:
            data = Time.objects.get(user=user)
            data.time = data.time - used_time
            data.save()
            response = {
                "status": "success",
                "time": data.time
            }
        return response


@method_decorator(csrf_exempt, name='dispatch')
class ExtensionRegistration(View):

    @method_decorator(token_validation)
    def get(self, *args, **kwargs):
        ext = self.request.GET.get('ext', None)
        user = args[1]
        if not ext:
            response = {
                "status": "failed",
                "error": "please provide extesion id"
            }
        else:
            try:
                Extension.objects.create(user=user, extension=ext)
                response = {
                    "status": "success",
                    "info": "extension registered"
                }
            except:
                response = {
                    "status": "failed",
                    "error": "failed to register app"
                }
        return JsonResponse(response)
