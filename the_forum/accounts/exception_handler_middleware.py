from django.http import HttpResponse
from django.shortcuts import redirect


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 500:
            return HttpResponse('Bad Request')
            # return redirect(request, 'templates/error_templates/500.html')
        return response
    return middleware
