from django import forms
from django.forms import ModelForm
from models import Todos
# we haev to create a form for creating todoapp

class TodoCreateForm(forms.Form):
    task_name=forms.CharField()
    user=forms.CharField()
    choice=(("completed","completed"),
             ("notcompleted","notcompleted"))
    status=forms.ChoiceField(choices=choice)




class Book(forms.Form):

    B_Name=forms.CharField()
    B_Author=forms.CharField()
    B_price=forms.IntegerField()


# class TodoModelForm(forms.ModelForm):
#     class Meta:
#         model=Todos
#         fields=["task_name","status","user"]


        #brand
        #url = owner/brands => method=get : get html page for adding brand
        #                     method=post : {brand_name:"brandname"} (create a brand)
        #url = owner/brands/1=> method=get : display brand with id=1
        #                      method=post : update