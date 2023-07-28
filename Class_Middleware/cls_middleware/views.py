from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print("This is View!")
    return HttpResponse("Hello this is Views Pages!!")
