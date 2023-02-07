from django.shortcuts import render
from .forms import TrainerForm
from django.http import HttpResponse
from .models import TrainerModel
# Create your views here.
def TrainerVW(request):
    form=TrainerForm()
    if request.method=='POST':
        form=TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data is stored')

    return render(request,'trainerpro.html',{'form':form})

def TrainerUP(request,pk):
    data=TrainerModel.objects.get(empid=pk)
    form=TrainerForm(instance=data)
    if request.method=='POST':
        form=TrainerForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponse('data has been update')
    return render(request,'trainerupdate.html',{'form':form})