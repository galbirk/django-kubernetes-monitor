from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

clusters = [
    {
        'name' : 'cluster1',
        'id' : 'AFSDFJKDS124SDF',
        'nodes' : [{'name':'node1','state':'running'},{'name':'node2','state':'stopped'}]
    }

]
title = 'Monitor k8s'

@login_required
def monitor(request):
    context = {
        'clusters' : clusters,
        'title': title
    }
    return render(request, 'monitor/monitor.html',context)