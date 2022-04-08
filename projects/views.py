from django.shortcuts import render
from django.http import HttpResponse

from .models import Project, Review ,Tag

def projects(request):
    projects = Project.objects.all()
    noProjects = len(projects)
    context = {"projects":projects , "noProjects":noProjects}
    return render(request, "projects/projects.html",context)

    
def project(request , pk):
    projectObj = Project.objects.get(id=pk) 
    tags = projectObj.tag_id.all()
    return render(request, "projects/project.html",{"projectObj":projectObj,"tags": tags} )