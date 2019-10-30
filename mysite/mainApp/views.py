from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')

def contacts(request):
    return  render(request, 'mainApp/basic.html', {'values': ['E-mail:', 'test@test.test']})