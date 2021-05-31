from django.shortcuts import render,redirect
from todoapp.forms import TodoCreateForm,Book,TodoModelForm
from .models import Todos,Books
# Create your views here.
def index(request):
    return render(request,"index.html")


def create_todo(request):
    if request.method == "GET":
        form=TodoCreateForm()
        context={}
        context["form"]=form
        return render(request,"createtodo.html",context)
    elif request.method == "POST":
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            taskname=form.cleaned_data.get("task_name")
            user=form.cleaned_data.get("user")
            status=form.cleaned_data.get("choice")
            todo=Todos(task_name=taskname,status=status,user=user)
            todo.save()
            return render(request,"index.html")

def list_all_todos(request):
    todos=Todos.objects.all()
    context={}
    context["todos"]=todos
    return render(request,"listalltodos.html",context)


def update_todo(request,id):
    tod=Todos.objects.get(id=id)
    dict={
        "task_name": tod.task_name,
        "user": tod.user,
        "status":tod.status,
    }

    form=TodoCreateForm(initial=dict)
    context={}
    context["form"]=form
    if request.method == "POST":
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            task_name=form.cleaned_data.get("task_name")
            user=form.cleaned_data.get("user")
            status=form.cleaned_data.get("status")
            tod.task_name=task_name
            tod.user=user
            tod.status=status
            tod.save()
            return redirect("list")
    return render(request,"updatetodo.html",context)





def delete_todo(request,id):
    todo=Todos.objects.get(id=id)
    todo.delete()
    return redirect("list")

# BOOK FIELD FROM HERE

def Create_Book(request):
    if request.method=="GET":
        book=Book()
        context={}
        context["book"]=book
        return render(request,"Book_Create.html",context)
    elif request.method=="POST":

        books=Book(request.POST)
        if books.is_valid():

            B_Name = books.cleaned_data.get("B_Name")
            B_Author = books.cleaned_data.get("B_Author")
            B_price = books.cleaned_data.get("B_price")
            book = Books(B_Name=B_Name, B_Author=B_Author, B_price=B_price)
            book.save()
            return render(request, "index.html")


def list_all_books(request):
    books=Books.objects.all()
    context={}
    context["books"]=books
    return render(request,"Book_List.html",context)

def B_Delete(request,id):
    bdel=Books.objects.get(id=id)
    bdel.delete()
    return redirect("listbooks")




#