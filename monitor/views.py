from django.shortcuts import render
from django.http import HttpResponse
from users.models import User_Role
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests

clusters = [
    {
        'name' : 'cluster1',
        'id' : 'AFSDFJKDS124SDF',
        'nodes' : [{'name':'node1','state':'running'},{'name':'node2','state':'stopped'}]
    }

]
def get_clusters():
    API_KEY = '22c29be96ab2f6a3d43d714f6329ae1151eb92781fd472a83fa248b82fbeb51b'
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

title = 'Monitor k8s'

@login_required
def monitor(request):
    #role = get_role(request)
    clusters = get_clusters()
    max_columns = 4
    interval = len(clusters) / max_columns
    rows = interval + 1
    if request.user.is_superuser:
        context = {
        'clusters' : clusters,
        'title': title
        }
    else:
        rows = rows
    return render(request, 'monitor/monitor.html',context)