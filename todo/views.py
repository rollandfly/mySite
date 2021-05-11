from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import ToDoList, Item
from .forms import CreateNewList, CreateNewItem

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def viewListPage(request):
    ls = ToDoList.objects.all()

    form = CreateNewList()

    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)

        return HttpResponseRedirect("/viewList/%i" % t.id)


    context={'liste':ls,'form':form}

    return render(request, "todo/viewList.html", context)

@login_required(login_url='/login')
def viewDetailPage(request, id):
    todolist = ToDoList.objects.get(id=id)
    if todolist in request.user.todolist.all():
        if request.method == "POST":
            if request.POST.get("save"):
                for item in todolist.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif request.POST.get("newItem"):
                text = request.POST.get("new")
                if len(text) > 2:
                    todolist.item_set.create(text=text, complete=False)
                else:
                    print("invalid")

        return render(request, "todo/detailList.html", {"ls": todolist})

    return render(request, "todo/detailList.html", {})
