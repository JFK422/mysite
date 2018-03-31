from django.shortcuts import render

def index(request):
    return render(request, 'index/indexSite.html', {'section':'home'})