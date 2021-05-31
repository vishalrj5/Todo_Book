from django.db import models

# Create your models here.

# closly related to database tables

# create table Todos (id int, task_name varchar(50),status varchar(20),user varchar(25);
# model class create

class Todos(models.Model):
    task_name=models.CharField(max_length=150)
    status=models.CharField(max_length=15,default="notompleted")
    user=models.CharField(max_length=250)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.task_name

class Books(models.Model):

    B_Name=models.CharField(max_length=200)
    B_Author=models.CharField(max_length=150)
    B_price=models.IntegerField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.B_Name
    # ORM queries

#O1 ) RM query for creating an object
# reference_name=className(fieldname=value,fieldname=value)
# reference.save()
# todo=Todos(task_name="Gas Payment",status="Not Completed",user="ajay")
# todo.save()

# to open shell
# python manaege.py shell



# 2 ) ORM query for fetching all records
# reference_name=className.objects.all()
# todos=Todos.objects.all()

#t3 ) odos created by user ajay
# Filtering

# refname=modelname.objects.filter(field=value)
# todos=Todos.objects.filter(user='ajay')



# 4 ) fetching record with id=4
# tod=todos.objects.get(id=4) //for filtering only for a single record


# 5 ) update ORM with id = 3 and set status=completed
# fetch objects with id=3 and then update

# todo=Todos.objects.get(id=3)
# todo.status="completed"
# todo.save()

# 6 ) Deleting an object
# first fetch it , then delete
# todo=Todos.objects.get(id=3)
# todo.delete()


# 7 ) Less than
# todos=Todos.objects.filter(date__lt=2021-05-28)


# book(book_name,author,price) , list , create , delete