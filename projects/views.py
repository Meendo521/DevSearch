from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import search_projects, paginate_projects


# Create your views here.
def projects(request):
    projects, search_query = search_projects(request)

    custom_range, projects = paginate_projects(request, projects, 6)

    context = {
        "projects": projects,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "projects/projects.html", context)


# view single project
def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    # tags = projectobj.tags.all()
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectobj
        review.owner = request.user.profile
        review.save()

        # update project vote count
        projectobj.get_vote_count
        messages.success(request, "Your review was successfully submitted")
        return redirect('project',pk=projectobj.id)

    context = {"project": projectobj, "form": form}
    return render(request, "projects/single-project.html", context)


# Create project
@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect("account")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


# Update project
@login_required(login_url="login")
def update_project(request, pk):
    profile = request.user.profile
    # get project per profile
    project = profile.project_set.get(id=pk)
    # get project to update by id
    # project = Project.objects.get(id=pk)
    # pass project id into form
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid:
            form.save()
            return redirect("account")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


# Delete project
@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("account")

    context = {"object": project}
    return render(request, "delete_template.html", context)
