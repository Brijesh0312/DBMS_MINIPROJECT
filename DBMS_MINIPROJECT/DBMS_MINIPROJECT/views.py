from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from dbms_main.models import question
from dbms_main.models import student_profile
from dbms_main.models import teacher_profile

currStudentLoggedIn=None
currTeacherLoggedIn=None
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

def teacherindex(request):
    return render(request,'index.html')
def teacherlogin(request):
    global currTeacherLoggedIn
    print("hello")
    name = request.POST['username']
    password = request.POST['pass']
    flag = False
    lst = teacher_profile.objects.all()
    for i in lst:
        if (i.name == name and i.password == password):
            currTeacherLoggedIn = i
            flag = True
    flag1 = not flag
    params = {'passcheck': flag1, 'currTeacherLogged': currTeacherLoggedIn}
    if (flag):
        return HttpResponseRedirect('TeacherHome')
    else:
        return render(request, 'index.html', params)
    # return render(request, 'index.html')

def teacherhome(request):
    return render(request,'teacherhome.html')
def teacherprofile(request):
    return render(request,'techerprofilepage.html',{'curr1' :currTeacherLoggedIn})
def teacherquestion(request):
    return render(request,'Answeringpage.html')
def teacheranswered(request):
    return render(request,'Answersubmitted.html')
def teachercontact(request):
    return render(request,'Contactpage.html')
def teacherLogout(request):
    return render(request,'teacherloggedout.html')
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