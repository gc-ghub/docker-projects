from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Stark Industries ⚙️</h1><p>Innovating the future, one line of code at a time.</p>")

