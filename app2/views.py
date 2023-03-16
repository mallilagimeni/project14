from django.shortcuts import render

# Create your views here.
def app2_first(request):
    return render(request,'app2_first.html')


def app2_sec(request):
    return render(request,'app2_sec.html')