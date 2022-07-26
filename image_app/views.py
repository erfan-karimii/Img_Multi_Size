from django.shortcuts import render 
from .models import DiffSize 
# Create your views here.
def test_view(request):
    context = {
        'posts' : DiffSize.objects.all() 
    }
    return render(request,'index.html',context)