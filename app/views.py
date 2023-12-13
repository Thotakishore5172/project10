from django.shortcuts import render

# Create your views here.

def ifblock(request):
    d={'n':10}
    return render(request,'ifblock.html',d)