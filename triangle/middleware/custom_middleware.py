from triangle.models import Logs


class LogMiddleware:
    def __init__(self, get_response):
        self.stdout = None
        self.style = None
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        if not request.path.startswith('/admin'):
            Logs(path=request.path, method=request.method).save()
        else:
            print(f'{request.path} - Warning: admin request will not be save')
