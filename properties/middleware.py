from . filters import PropertyFilter
from . models import Property


class PropertyMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            qs = Property.objects.filter(is_available=True)
            request.filter = PropertyFilter(request.GET, queryset=qs)
        except Exception as e:
            print(e)

        return None

