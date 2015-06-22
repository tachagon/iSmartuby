from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    template = 'authen/index.html'
    context = {}
    return render(
        request,
        template,
        context
    )
