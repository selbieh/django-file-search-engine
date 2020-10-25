from django.shortcuts import render
from .models import StoredFiles
from django.shortcuts import get_object_or_404

def retrive(request,obj_id):
    obj=get_object_or_404(StoredFiles,id=obj_id)
    return render(request,"search/retive_searche.html",context={"obj":obj})
# Create your views here.
