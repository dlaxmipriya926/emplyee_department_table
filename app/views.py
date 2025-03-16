from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
# Create your views here
def display_dept(request):
    TDO=Dept.objects.all()
    d={'TDO':TDO}
    return render(request,'insert_dept.html',d)

def display_emp(request):
    TEO=Emp.objects.all()
    TEO=Emp.objects.filter(job='MANAGER')
    TEO=Emp.objects.exclude(job='MANAGER')
    TEO=Emp.objects.all()[1:2:]
    TEO=Emp.objects.all()[::-1]
    TEO=Emp.objects.all().order_by('sal')
    TEO=Emp.objects.all().order_by('-ename')

    TEO=Emp.objects.all().order_by(Length('ename'))
    TEO=Emp.objects.all().order_by(Length('ename').desc())
    d={'TEO':TEO}
    return render(request,'insert_emp.html',d)

def insert_dept(request):
    deptno=int(input('enter deptno'))
    dname=input('enter dname')
    loc=input('enter location')

    DO=Dept.objects.get_or_create(deptno=deptno,dname=dname,loc=loc)

    if DO[1]:
        return HttpResponse('DO is created')
    else:
        return HttpResponse('DO is already created')
    
def insert_emp(request):
    empno=int(input('enter empno'))
    ename=input('enter ename')
    job=input('enter job')
    mgr=input('enter mgrno')
    if mgr:
        MO=Emp.objects.get(empno=int(mgr))
    else:
        MO=None
    sal=float(input('enter salary'))
    comm=input('enter comm')
    if comm:
        comm=float(comm)
    else:
        comm=None
    deptno=int(input('enter deptno'))
    DO=Dept.objects.get(deptno=deptno)
    
    hiredate=input('enter date')
    EO=Emp.objects.get_or_create(empno=empno,ename=ename,job=job,sal=sal,comm=comm,hiredate=hiredate,deptno=DO,mgr=MO)
    if EO[1]:
        return HttpResponse('EO is created')
    else:
        return HttpResponse('EO is already present')