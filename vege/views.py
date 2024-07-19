from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_image=request.FILES.get('receipe_image')
        receipe_description=data.get('receipe_description')
        Recipe.objects.create(
            receipe_name=receipe_name,
            receipe_image=receipe_image,
            receipe_description=receipe_description,
        )

        return redirect("/receipes/") 
    # print(receipe_name)
    # print(receipe_image)
    # print(receipe_description)
    queryset=Recipe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context ={'receipes':queryset}
    return render(request,'receipes.html',context)
 
def update_receipe(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_image=request.FILES.get('receipe_image')
        receipe_description=data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect("/receipes/")
    context={'receipe':queryset}
    return render(request,'update_receipes.html',context)

def delete_receipe(request,id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes/")
