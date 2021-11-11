from django.http import HttpResponse
from django.shortcuts import render
from dbms_main.models import question

def index(request):
    return render(request,'StudentLoginPage.html')

def home(request):
    return render(request,'studentPage.html')

def profile(request):
    return render(request,'profilepage.html')

def doubts(request):
    return render(request,'doubtspage.html')

def answers(request):
    return render(request,'ShowAnswerspage.html')

def contact(request):
    return  render(request,'contactsPage.html')

def logout(request):
    return render(request,'LoggedOut.html')

def doubtsubmit(request):
    if request.method == 'POST':
        que=request.POST['disc']
        depart=request.POST['department']
        sub=request.POST['subject']
        print(depart)
        print(sub)

    return render(request,'doubtspage.html')