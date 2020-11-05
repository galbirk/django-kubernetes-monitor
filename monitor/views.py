from django.shortcuts import render
from django.http import HttpResponse

clusters = [
    {
        'name' : 'cluster1',
        'id' : 'AFSDFJKDS124SDF',
        'nodes' : [{'name':'node1','state':'running'},{'name':'node2','state':'stopped'}]
    }

]
title = 'Monitor k8s'
def login(request):
    return render(request, 'monitor/login.html', {'title': title})

def monitor(request):
    context = {
        'clusters' : clusters,
        'title': title
    }
    return render(request, 'monitor/monitor.html',context)