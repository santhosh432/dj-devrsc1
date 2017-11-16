# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

# Create your views here.


from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponseRedirect

from models import *

from forms import UserRegistrationForm, ExfinalForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required  # login require decorator...........

from django.db.models import Q

from django.db.models import Sum

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # for pagination

from django.forms import formset_factory

import time

milsec = int(round(time.time() * 1000))

# Create your views here.
# This is htmlpage with HttpResponse, (required :from django.http import HttpResponse)
'''
def home(request):
    return HttpResponse("This is home page")
'''


# This is html page with render ,(required:from django.shortcuts import render)

def check(request):
    return render(request, 'check.html')


def home(request):
    return render(request, "home.html")


def homepage(request):
    return render(request, "home.html")


def registration(request):
    return render(request, "registration.html")


def add_user(request):
    username = request.POST.get("username")
    email = request.POST.get("emailid")
    password = request.POST.get("password")
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    address = request.POST.get("address")
    phone = request.POST.get("phone")
    tech = request.POST.get("tech")
    print ('.........address........', address)
    if request.method == 'GET':
        print ('get here')
        form = UserRegistrationForm()  # object creation
    else:
        print ('form in post')
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print ('user registration from valid')
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            a = UserProfile(user_id=user.id, address=address, phone=phone, tech=tech)
            a.save()
            print ('saved')
            return HttpResponseRedirect('/homepage/')
    return render(request, 'registration.html', {'form': form, })


def login_check(request):
    request.session['userid'] = request.user.id

    print ("user id:", request.session['userid'])
    return render(request, "adminP2.html")


# list of technolgies..................
def add_tech(request):
    sub = request.POST.get("subject")
    time = request.POST.get("timelimit")
    errors = []
    listsub = Techlist.objects.all()

    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter the question here:')
        if not request.POST.get('timelimit', ''):
            errors.append('select time limit')
        if not errors:
            t = Techlist(subjectname=sub, timelimit=time)
            t.save()

            return redirect('/loginverify/addtechnology/', {'tech': listsub})

    return render(request, "adminP21.html", {'errors': errors, 'tech': listsub})


# list of questions........................
def add_quest(request):
    question = request.POST.get("question")
    a = request.POST.get("a")
    b = request.POST.get("b")
    c = request.POST.get("c")
    d = request.POST.get("d")
    ro = request.POST.get("ro")
    tech = request.POST.get("tech")

    techlist = Techlist.objects.all()

    quelist = Questionslist.objects.all()
    errorsget = []
    if request.method == 'POST':

        if not request.POST.get('question', ''):
            errorsget.append('Enter question:')
        if not request.POST.get('a', ''):
            errorsget.append('choose option A:')
        if not request.POST.get('b', ''):
            errorsget.append('choose option B:')
        if not request.POST.get('c', ''):
            errorsget.append('choose option C:')
        if not request.POST.get('d', ''):
            errorsget.append('choose option D:')
        if not request.POST.get('ro', ''):
            errorsget.append('choose right option :')
        if not request.POST.get('tech', ''):
            errorsget.append('choose technology:')

        if not errorsget:
            qi = Questionslist(question=question, a=a, b=b, c=c, d=d, subtype=tech, ro=ro)
            qi.save()
            return redirect('/loginverify/enterques/', {'que': quelist, 'errors': errorsget})

    return render(request, "adminP3.1.html", {'tech': techlist, 'que': quelist, 'errors': errorsget})


def status(request):
    cs = Techlist.objects.all()

    return render(request, "adminP4.1.html", {'getstatus': cs})


def statusupdate(request):
    li = []
    actlist = request.POST.get("adstatus")
    if actlist in "Active":
        li.append(actlist)
    return render(request, "check.html", {"listof": li, "actl": actlist})


def results(request):
    return render(request, "adminP5.1.html")


def edit_tech(request):
    techid = request.POST.get('techid')

    techeditlist = Techlist.objects.get(pk=techid)
    t1 = techeditlist.subjectname
    t2 = techeditlist.timelimit
    t3 = techeditlist.id

    return render(request, "adminP2.2.html", {'t1': t1, 't2': t2, 't3': t3, 'idcheck': techeditlist})


def updatetechlist(request):
    upt = Techlist.objects.get(id=request.POST.get('udtechid'))
    newtech = request.POST.get('upsub')

    newtimer = request.POST.get('uptimer')
    upt.subjectname = newtech
    upt.timelimit = newtimer
    upt.save()
    listsub = Techlist.objects.all()
    print (listsub)
    return render(request, "adminP21.html", {'tech': listsub})


def questentry_tech(request):
    return render(request, "adminP3.1.html")


def student_first_page(request):
    return render(request, "studentP2.html")


def starttest(request):
    stid = UserProfile.objects.get(pk=request.user.id)
    sttech = stid.tech
    userid = stid.id

    # pagination code start...........
    # products1=Product.objects.order_by('?')[:30]
    # qpag = Questionslist.objects.filter(Q(subtype=sttech))

    # paginator = Paginator(qpag, 1) # here products1 is objcet
    # page = request.GET.get('page')
    # try:
    #     qpagination = paginator.page(page) # here product is the paginator object
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     qpagination = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     qpagination = paginator.page(paginator.num_pages)

    # pagination code end...........





    # Q(subjectname="aptitude") | Q(subjectname="reasoning") | Q(subjectname=sttech)
    qp = Questionslist.objects.filter(Q(subtype="apt") | Q(subtype="Resoning") | Q(subtype=sttech))
    '''
    timer1 = Techlist.objects.get(subjectname="aptitude")
    timer2 = Techlist.objects.get(subjectname="reasoning")
    timer3 = Techlist.objects.get(subjectname=sttech)
    tottimer =timer1.timelimit+timer2.timelimit+timer3.timelimit
    '''
    timer = Techlist.objects.filter(
        Q(subjectname="aptitude") | Q(subjectname="reasoning") | Q(subjectname=sttech)).aggregate(Sum('timelimit'))
    tottimer = timer['timelimit__sum']

    return render(request, "studentP3.html",
                  {'qeslist': qp, "studenttech": sttech, "fronttimer": tottimer, "stid": userid})
    # return render(request, "studentP3.html",{'qeslist':qpagination,"studenttech":sttech,"fronttimer":tottimer,"stid":userid})


def acknowledgment(request):
    # context = RequestContext(request)

    # stid = UserProfile.objects.get(pk=request.POST.get("empid"))
    # authid = User.objects.get(pk=request.POST.get("empid"))
    try:
        d = request.session['userid']
    except:
        return redirect('/homepage')

    stid = UserProfile.objects.get(pk=request.user.id)
    authid = User.objects.get(pk=request.user.id)
    stuid = int(stid.id)
    sttech = stid.tech
    stemailid = authid.email
    print (request.POST)
    val = dict(request.POST)
    print (val)
    keylist = val.keys()
    print (keylist)
    d = val
    stdackdet = Empanswerslist.objects.filter(empid=stuid)

    totque = Questionslist.objects.filter(Q(subtype="apt") | Q(subtype="Resoning") | Q(subtype=sttech)).count()
    print (totque)
    print (d['orginalans'])
    answers_attempted = []
    score = 0
    c = 1

    tid = int(str(milsec) + str(stuid))

    for h, i in (zip(d['orginalans'], d['question_id'])):
        o = "opt" + str(c)
        print (o)
        c = c + 1
        if o in keylist:
            s = d[o]
            s = "".join(d[o])
            answers_attempted.append(s)

        else:
            s = "N"

        print ("original Answer:", h, "user answer:", s, "Question ID:", i, sttech, stemailid)
        stdack = Empanswerslist(empid=stuid, empanswer=s, originalanswer=h, empqueid=i, emptech=sttech,
                                empmailid=stemailid, testid=1)
        stdack.save()

        if h == s:
            score = score + 1

    count_att = len(answers_attempted)
    print (score, count_att)
    print ("#############################")

    stdackdet = Empanswerslist.objects.filter(empid=stuid)

    del request.session['userid']  # to clear session

    return render(request, "studentP4.html",
                  {"stdet": stdackdet, "message": "ok...", "usermail": stemailid, "totquestions": totque,
                   "score": score, "stuid": stuid, "attempted": count_att, 'sttech': sttech})


def acknowledgmentfinal(request):
    return render(request, "studentP4.html",
                  {"stdet": stdackdet, "message": "ok...", "usermail": stemailid, "totquestions": totque,
                   "score": score, "stuid": stuid})


