# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MemberForm
from .models import Member
from visual.models import MainVisual


# Create your views here.

@login_required
def memadd(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)

        if form.is_valid():
            # new member added but not confirmed by admin
            new_entry = form.save(commit=False)
            new_entry.head = request.user
            form.save(commit=True)
            memdetails = Member.objects.filter(head=request.user)
            return render(request, 'member/memlist.html', {'memlist': memdetails})
    else:
        form = MemberForm()
    return render(request, 'member/memberadd.html', {'form': form})


# fetching member details for user to see who are added
@login_required
def status(request):
    memdetails = Member.objects.filter(head=request.user)
    return render(request, 'member/memlist.html', {'memlist': memdetails})


def visualise(request):
    pop = []
    male = []
    female = []
    mainv = MainVisual.objects.order_by('year')
    for v in mainv:
        pop.append(v.totalpop)
        male.append(v.male)
        female.append(v.female)

    currmale = Member.objects.filter(request_status=True, sex='Male')
    curmale = ['Male', currmale.count()]
    currfemale = Member.objects.filter(request_status=True, sex='Female')
    curfemale = ['Female', currfemale.count()]
    return render(request, 'visualisation.html', {'pop':pop, 'male':male, 'female':female,
                                                  'curmale':curmale, 'curfemale':curfemale})


def censusvisual(request):
    currmale = Member.objects.filter(request_status=True)
    curmale = currmale.count()
    return render(request, 'censusvisual.html', {'curmale':curmale})
