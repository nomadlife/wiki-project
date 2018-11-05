from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, 'wikipage/home.html', {'title':'HOME'})

def about(request):
    return render(request, 'wikipage/about.html', {'title':'About'})  