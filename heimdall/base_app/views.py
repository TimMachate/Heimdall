from django.shortcuts import render
from .models import navbar

# Create your views here.
def index(request):
    nav = navbar.objects.all()
    index = {}
    for i in nav:
        if i.index1 not in index:
            index[i.index1] = {}
        if i.index2 not in index[i.index1]:
            index[i.index1][i.index2] = []
        index[i.index1][i.index2].append(i.index3)

    content = {
        'index' : index,
    }
    return render(request,'index.html',content)