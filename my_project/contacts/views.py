from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ContactForm
from .models import Contact
# Create your views here.

def contact_create(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("name")
        instance.save()
        messages.success(request, "Successfully Created!")
        return HttpResponseRedirect(instance.get_absolute_url())   
    context = {
        "form": form,
    }
    return render(request,"contact_form.html",context)

def contact_detail(request, id=None):
    instance = get_object_or_404(Contact, id=id)
    context = {
        "instance":instance
    }
    return render(request,"contact_detail.html",context)

def contact_list(request):
    queryset = Contact.objects.all().order_by("name")
    context = {
        "object_list":queryset,
        "title":"Contact List"
    } 
    return render(request,"contact_list.html",context)

def contact_update(request, id=None):
    instance = get_object_or_404(Contact, id=id)
    form = ContactForm(request.POST or None,  request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Entry Updated!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title":instance.name,
        "instance":instance,
        "form":form,
    }
    return render(request,"contact_form.html", context)

def contact_delete(request, id=None):
    instance = get_object_or_404(Contact, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("contacts:list")
    