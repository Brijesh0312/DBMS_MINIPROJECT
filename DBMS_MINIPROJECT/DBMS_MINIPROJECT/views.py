from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from dbms_main.models import question
from dbms_main.models import student_profile

currStudentLoggedIn=None
def index(request):

    return render(request,'StudentLoginPage.html')

def studentLogin(request):
    global currStudentLoggedIn
    print("hello")
    name = request.POST['user']
    password = request.POST['pass']
    flag = False
    lst = student_profile.objects.all()
    for i in lst:
        if (i.name == name and i.password == password):
            currStudentLoggedIn = i
            flag = True
    flag1 = not flag
    params = {'passcheck': flag1, 'currStudentLogged': currStudentLoggedIn}
    if (flag):
        return HttpResponseRedirect('studenthome')
    else:
        return render(request, 'StudentLoginPage.html', params)


def home(request):
    return render(request,'studentPage.html')

def profile(request):

    return render(request,'profilepage.html',{'curr':currStudentLoggedIn})

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
        if currStudentLoggedIn:
            que=request.POST['disc']
            depart=request.POST['department']
            sub=request.POST['subject']
            ques=question(description=que,department=depart,subject=sub,stud_id=currStudentLoggedIn)
            ques.save()

            return render(request,'doubtSubmitted.html')
        return HttpResponseRedirect('StudentLogin')
    return HttpResponseRedirect('StudentLogin')