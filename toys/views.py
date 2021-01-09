from django.http import HttpResponse


def dashboard(request):
    return HttpResponse("Welcom to Alltoys")