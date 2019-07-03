from django.shortcuts import render,HttpResponseRedirect
from django.forms import modelformset_factory
from .models import Qurilish




def hi(request):

    QurilishFormSet = modelformset_factory(Qurilish, fields=('q_type', 'servise_name', 'servise_code', 'soato', 'report_month', 'report_year', 'last_year'), extra=1)
    if request.method == "POST":
        form = QurilishFormSet(request.POST)
        instance = form.save()
    form = QurilishFormSet()




    return render(request, 'app1/home.html',{'form':form})




