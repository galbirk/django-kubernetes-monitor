from django.shortcuts import render
from django.http import HttpResponse
from users.models import User_Role
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests
import os

clusters = [
    {
        'name' : 'cluster1',
        'id' : 'AFSDFJKDS124SDF',
        'nodes' : [{'name':'node1','state':'running'},{'name':'node2','state':'stopped'}]
    }

]
def get_clusters():
    API_KEY = os.getenv('API_KEY')
    url = 'https://api.digitalocean.com/v2/kubernetes/clusters'
    headers = {'Content-type': 'application/json' ,'Authorization': f'Bearer {API_KEY}'}
    r = requests.get(url, headers=headers)
    json = r.json()
    clusters = json['kubernetes_clusters']
    return clusters

def get_role(request):
    user = User.objects.filter(username=request.user.username).first()
    role = User_Role.objects.filter(user=user).first()
    return role

def assign_clusters(role,clusters,request):
    assigned_clusters = []
    for cluster in clusters:
        tags = cluster['tags']
        for tag in tags:
            if tag == f'{role}:{request.user.username}':
                assigned_clusters.append(cluster)
                break
    return assigned_clusters

title = 'Monitor k8s'

@login_required
def monitor(request):
    role = get_role(request)
    clusters = get_clusters()
    if  not request.user.is_superuser:
        clusters = assign_clusters(role,clusters,request)
    context = {
        'clusters' : clusters,
        'title': title
        }
    return render(request, 'monitor/monitor.html',context)