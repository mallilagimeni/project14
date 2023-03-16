from django.shortcuts import render

# Create your views here.
def app1_first(request):
    return render(request,'app1_first.html')

def app1_sec(request):
    return render(request,'app1_sec.html')