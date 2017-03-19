from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from.models import Time


@method_decorator(csrf_exempt, name='dispatch')
class UserData(View):

    def get(self, *args, **kwargs):
        fct = self.request.GET.get('fct', None)

        if fct == "get_data":
            response = self.get_data()
        elif fct == "update_data":
            response = self.update_data()
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

    def get_data(self):
        try:
            data = Time.objects.get(user=self.request.user)
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

    def update_data(self):
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
            data = Time.objects.get(user=self.request.user)
            data.time = data.time - used_time
            data.save()
            response = {
                "status": "success",
                "time": data.time
            }
        return response
