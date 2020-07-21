from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import util
from re import search
from django import forms
from django.urls import reverse
import random

def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def search(request):
    if request.method == 'POST':
        title = request.POST.get('search')
        if title in util.list_entries():
            content = util.get_entry(title)
            return render(request,"encyclopedia/search.html", {
            "name": content,
            "title":title})
        else:
            elements=Filter(util.list_entries(),title)
            if elements:
                return render(request, "encyclopedia/index.html", {
                "entries":elements})
            else:
                return render(request, "encyclopedia/error.html")

            
            
def Filter(string, substr): 
    return [str for str in string if
             any(sub in str for sub in substr)] 

class NewTaskForm(forms.Form):
    title= forms.CharField(label="title")
    content= forms.CharField( label="content",widget=forms.Textarea (attrs={'placeholder':'paste your article here'}))

def create(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title in util.list_entries():
                return render(request,"encyclopedia/error.html")
                
            util.save_entry(title,content)
            return HttpResponseRedirect(reverse("wiki:index"))
        else:
            return render(request,"encyclopedia/create.html", {
        "form": form })
    return render(request,"encyclopedia/create.html", {
        "form": NewTaskForm()})

def edit(request):
    if request.method == 'POST':
        title= request.POST.get("title")
        content= request.POST.get("content")
        util.save_entry(title,content)
    return HttpResponseRedirect(reverse("wiki:index"))
            
def randompage(request):
    myurls=[
        "Python",
        "CSS",
        "C",
        "Django",
        "Git",
        "HTML"
        ]
    file=random.choice(myurls)
    return render(request,f"encyclopedia/{file}.html")
        
    
