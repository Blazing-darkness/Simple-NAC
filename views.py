from django.shortcuts import render, redirect
from .forms import NasForm, RadacctForm, RadcheckForm, RadgroupcheckForm, RadgroupreplyForm, RadpostauthForm, RadreplyForm, RadusergroupForm
from .forms import NasFormL, RadacctFormL, RadcheckFormL, RadgroupcheckFormL, RadgroupreplyFormL, RadpostauthFormL, RadreplyFormL, RadusergroupFormL
from .models import Nas, Radacct, Radcheck, Radgroupcheck, Radgroupreply, Radpostauth, Radreply, Radusergroup
import os
# Create your views here.

def radius(request):
    return render(request, 'Radius/home.html')

#---------------------------------------------------------------------------------------------------------

def NasAnlegen(request):
    if request.method == 'POST':
        print("1!")
        form = NasForm(request.POST)
        if form.is_valid():
            form.save()
            inhalt = form.cleaned_data.get('description')
            print(inhalt)
            return redirect('Seite_02')
    else:
        print("2!")
        form = NasForm(request.POST)
        print(form)
    return render(request, 'Radius/NasAnlegen.html', {'form': form})


def NasAnzeigen(request):
    if request.method == 'POST':
        form = NasFormL(request.POST)
        if form.is_valid():
            idL = form.cleaned_data.get('id')
            Nas.objects.filter(id=idL).delete()
            return redirect('Seite_02')
    else:
        form = NasFormL(request.POST)
        print(form)
    return render(request, 'Radius/NasAnzeigen.html', {'Nas': Nas.objects.all(), 'form': form})

#----------------------------------------------------------------------------------------------------------

def RadacctAnlegen(request):
    if request.method == 'POST':
        print("1!")
        form = RadacctForm(request.POST)
        if form.is_valid():
            form.save()
            inhalt = form.cleaned_data.get('description')
            print(inhalt)
            return redirect('Seite_04')
    else:
        print("2!")
        form = RadacctForm(request.POST)
        print(form)
    return render(request, 'Radius/RadacctAnlegen.html', {'form': form})

def RadacctAnzeigen(request):
    if request.method == 'POST':
        form = RadacctFormL(request.POST)
        if form.is_valid():
            idL = form.cleaned_data.get('id')
            Radacct.objects.filter(id=idL).delete()
            return redirect('Seite_04')
    else:
        form = RadacctFormL(request.POST)
        print(form)
    return render(request, 'Radius/RadacctAnzeigen.html', {'Radacct': Radacct.objects.all(), 'form': form})

#---------------------------------------------------------------------------------------------------------

def RadcheckAnlegen(request):
    if request.method == 'POST':
        print("1!")
        form = RadcheckForm(request.POST)
        if form.is_valid():
            form.save()
            inhalt = form.cleaned_data.get('description')
            print(inhalt)
            return redirect('Seite_06')
    else:
        print("2!")
        form = RadcheckForm(request.POST)
        print(form)
    return render(request, 'Radius/RadcheckAnlegen.html', {'form': form})

def RadcheckAnzeigen(request):
    if request.method == 'POST':
        form = RadcheckFormL(request.POST)
        if form.is_valid():
            idL = form.cleaned_data.get('id')
            Radcheck.objects.filter(id=idL).delete()
            return redirect('Seite_06')
    else:
        form = RadcheckFormL(request.POST)
        print(form)
    return render(request, 'Radius/RadcheckAnzeigen.html', {'Radcheck': Radcheck.objects.all(), 'form': form})

#--------------------------------------------------------------------------------------------------------

def RadgroupcheckAnlegen(request):
    if request.method == 'POST':
        print("1!")
        form = RadgroupcheckForm(request.POST)
        if form.is_valid():
            form.save()
            inhalt = form.cleaned_data.get('description')
            print(inhalt)
            return redirect('Seite_08')
    else:
        print("2!")
        form = RadgroupcheckForm(request.POST)
        print(form)
    return render(request, 'Radius/RadgroupcheckAnlegen.html', {'form': form})

def RadgroupcheckAnzeigen(request):
    if request.method == 'POST':
        form = RadgroupcheckFormL(request.POST)
        if form.is_valid():
            idL = form.cleaned_data.get('id')
            Radgroupcheck.objects.filter(id=idL).delete()
            return redirect('Seite_08')
    else:
        form = RadgroupcheckFormL(request.POST)
        print(form)
    return render(request, 'Radius/RadgroupcheckAnzeigen.html', {'Radgroupcheck': Radgroupcheck.objects.all(), 'form': form})

#-----------------------------------------------------------------------------------------------------------

def RadgroupreplyAnlegen(request):
    if request.method == 'POST':
        print("1!")
        form = RadgroupreplyForm(request.POST)
        if form.is_valid():
            form.save()
            inhalt = form.cleaned_data.get('description')
            print(inhalt)
            return redirect('Seite_10')
    else:
        print("2!")
        form = RadgroupreplyForm(request.POST)
        print(form)
    return render(request, 'Radius/RadgroupreplyAnlegen.html', {'form': form})

def RadgroupreplyAnzeigen(request):
    if request.method == 'POST':
        form = RadgroupreplyFormL(request.POST)
        if form.is_valid():
            idL = form.cleaned_data.get('id')
            Radgroupreply.objects.filter(id=idL).delete()
            return redirect('Seite_10')
    else:
        form = RadgroupreplyFormL(request.POST)
        print(form)
    return render(request, 'Radius/RadgroupreplyAnzeigen.html', {'Radgroupreply': Radgroupreply.objects.all(), 'form': form})

#-----------------------------------------------------------------------------------------------------------

def RadpostauthAnlegen(request):
    if request.method == 'POST':
        print("1!")
        form = RadpostauthForm(request.POST)
        if form.is_valid():
            form.save()
            inhalt = form.cleaned_data.get('description')
            print(inhalt)
            return redirect('Seite_12')
    else:
        print("2!")
        form = RadpostauthForm(request.POST)
        print(form)
    return render(request, 'Radius/RadpostauthAnlegen.html', {'form': form})

def RadpostauthAnzeigen(request):
    if request.method == 'POST':
        form = RadpostauthFormL(request.POST)
        if form.is_valid():
            idL = form.cleaned_data.get('id')
            Radpostauth.objects.filter(id=idL).delete()
            return redirect('Seite_12')
    else:
        form = RadpostauthFormL(request.POST)
        print(form)
    return render(request, 'Radius/RadpostauthAnzeigen.html', {'Radpostauth': Radpostauth.objects.all(), 'form': form})

#-----------------------------------------------------------------------------------------------------------

def RadreplyAnlegen(request):
    if request.method == 'POST':
        print("1!")
        form = RadreplyForm(request.POST)
        if form.is_valid():
            form.save()
            inhalt = form.cleaned_data.get('description')
            print(inhalt)
            return redirect('Seite_14')
    else:
        print("2!")
        form = RadreplyForm(request.POST)
        print(form)
    return render(request, 'Radius/RadreplyAnlegen.html', {'form': form})

def RadreplyAnzeigen(request):
    if request.method == 'POST':
        form = RadreplyFormL(request.POST)
        if form.is_valid():
            idL = form.cleaned_data.get('id')
            Radreply.objects.filter(id=idL).delete()
            return redirect('Seite_14')
    else:
        form = RadreplyFormL(request.POST)
        print(form)
    return render(request, 'Radius/RadreplyAnzeigen.html', {'Radreply': Radreply.objects.all(), 'form': form})

#-----------------------------------------------------------------------------------------------------------

def RadusergroupAnlegen(request):
    if request.method == 'POST':
        print("1!")
        form = RadusergroupForm(request.POST)
        if form.is_valid():
            form.save()
            inhalt = form.cleaned_data.get('description')
            print(inhalt)
            return redirect('Seite_16')
    else:
        print("2!")
        form = RadusergroupForm(request.POST)
        print(form)
    return render(request, 'Radius/RadusergroupAnlegen.html', {'form': form})

def RadusergroupAnzeigen(request):
    if request.method == 'POST':
        form = RadusergroupFormL(request.POST)
        if form.is_valid():
            idL = form.cleaned_data.get('id')
            Radusergroup.objects.filter(id=idL).delete()
            return redirect('Seite_16')
    else:
        form = RadusergroupFormL(request.POST)
        print(form)
    return render(request, 'Radius/RadusergroupAnzeigen.html', {'Radusergroup': Radusergroup.objects.all(), 'form': form})

#-----------------------------------------------------------------------------------------------------------

def Apply(request):
    if request.method == 'POST':
        print("HaliHallo!")
        #os.system("sudo -s -p '' service freeradius restart < ~/file")
        instream = os.popen("sudo -S service freeradius restart", "w")
        instream.write("start123")
        instream.close()
        #os.system('start123')
        print("success!!!")
    return render(request, 'Radius/Apply.html')

#-----------------------------------------------------------------------------------------------------------

def CoA(request):
    return render(request, 'Radius/CoA.html')
