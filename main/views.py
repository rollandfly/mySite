from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'main/home.html',{})


def contactPage(request):
    return render(request, 'main/contact.html', {})
