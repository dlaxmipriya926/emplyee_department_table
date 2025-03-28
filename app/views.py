from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
from django.db.models import Prefetch
from django.db.models import Avg,Sum,Count,Max,Min



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

    # aggregate function
    avgsal=Emp.objects.aggregate(Avg('sal'))
    print(avgsal)
    sumsal=Emp.objects.aggregate(Sum('sal'))
    print(sumsal)
    maxsal=Emp.objects.aggregate(Max('sal'))
    print(maxsal)
    minsal=Emp.objects.aggregate(minsal=Min('sal'))
    print(minsal)
    avgsal=Emp.objects.filter(deptno=20).aggregate(Avg('sal'))
    print(avgsal)
    avgsal=Emp.objects.aggregate(agsal=Avg('sal'))['agsal']
    print(avgsal)

    # avgsal=Emp.objects.annotate(avgsal=Avg('sal'))[avgsal]

    

    # operators
    TEO=Emp.objects.all()
    TEO=Emp.objects.filter(job__startswith='M')
    TEO=Emp.objects.filter(sal__gt=2000)
    TEO=Emp.objects.filter(sal__lt=3000)
    TEO=Emp.objects.filter(hiredate__month='02')
    TEO=Emp.objects.filter(hiredate__year='2024')
    TEO=Emp.objects.filter(hiredate__gte='2025-03-13')
    TEO=Emp.objects.filter(hiredate__day='01')
    TEO=Emp.objects.filter(ename__startswith='A')
    TEO=Emp.objects.filter(ename__endswith='S')
    TEO=Emp.objects.filter(deptno__in=(50,30))
    TEO=Emp.objects.filter(job__contains='D')
    TEO=Emp.objects.filter(ename__regex='^A\w+S$')

    # Q class

    TEO=Emp.objects.filter(deptno=10,sal__gte=3000)
    TEO=Emp.objects.all()
    TEO=Emp.objects.filter(deptno=20,sal__gte=3000)
    TEO=Emp.objects.filter(Q(deptno=20)|Q(sal__gte=3000))

    TEO=Emp.objects.all()

    # raw querys
    
    TEO=Emp.objects.raw('SELECT * FROM app_Emp')
    TEO=Emp.objects.raw('SELECT * FROM app_Emp where ename="BLAKE" ')
    

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
    



    # join using select_related

def EmpToDeptJoin(request):
    QLEDO=Emp.objects.all().select_related('deptno')
    QLEDO=Emp.objects.select_related('deptno').filter(job='MANAGER')
    QLEDO=Emp.objects.select_related('deptno').filter(Q(job='MANAGER')& Q(sal__gt=2500))
    QLEDO=Emp.objects.select_related('deptno').filter(deptno__loc='DALLAS')
    QLEDO=Emp.objects.select_related('deptno').filter(Q(deptno__loc='DALLAS')&Q(sal__gte=3000))
    QLEDO=Emp.objects.select_related('deptno').filter(deptno=10)
    QLEDO=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    QLEDO=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    QLEDO=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    QLEDO=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    QLEDO=Emp.objects.select_related('deptno').filter(sal__range=(2000,3000))
    QLEDO=Emp.objects.select_related('deptno').filter(deptno__dname__in=('ACCOUNTING','SALES'))
    QLEDO=Emp.objects.select_related('deptno').filter(ename__startswith='s')
    QLEDO=Emp.objects.select_related('deptno').filter(Q(ename__startswith='s') | Q(job='CLERK'))
    QLEDO=Emp.objects.select_related('deptno').filter(ename__endswith='s')
    QLEDO=Emp.objects.select_related('deptno').filter(deptno=20)
    QLEDO=Emp.objects.select_related('deptno').filter(job='CLERK')
    QLEDO=Emp.objects.select_related('deptno').filter(deptno__dname='SALES')
    QLEDO=Emp.objects.select_related('deptno').filter(deptno__loc='NEW YORK')
    QLEDO=Emp.objects.select_related('deptno').filter(Q(deptno__loc='NEW YORK')&Q(sal__lt=2000))
    QLEDO=Emp.objects.select_related('deptno').filter(deptno__loc__startswith='d')

    d={'QLEDO':QLEDO}
    return render(request,'EmpToDeptJoin.html',d)

def EmpToMgrJoin(request):
    QLEMO=Emp.objects.all().select_related('mgr')
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__sal__gte=3000)
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__comm__isnull=True)
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__comm__isnull=False)
    QLEMO=Emp.objects.select_related('mgr').filter(sal__lt=3000)
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__deptno=20)
    QLEMO=Emp.objects.select_related('mgr').filter(Q(mgr__deptno=20) | Q(sal__gt=3000))
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__ename__startswith='s')
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__mgr__ename__startswith='s')
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__ename='SCOTT')
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__deptno=30)
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__job='MANAGER')
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__deptno=30)
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__deptno=20)
    QLEMO=Emp.objects.select_related('mgr').filter(ename__startswith='s')
    QLEMO=Emp.objects.select_related('mgr').filter(sal__gt=3000)
    QLEMO=Emp.objects.select_related('mgr').filter(Q(mgr__ename__startswith='s')&Q(deptno=20))
    QLEMO=Emp.objects.select_related('mgr').filter(Q(sal__gt=2000)|Q(job='CLERK'))
    QLEMO=Emp.objects.select_related('mgr').filter(job='SALESMAN')
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__hiredate='2025-03-13')
    QLEMO=Emp.objects.select_related('mgr').filter(hiredate='2024-03-13')

    d={'QLEMO':QLEMO}
    return render(request,'EmpToMgrJoin.html',d)


def EmpToDeptAndMgr(request):
    QLEDMO=Emp.objects.all().select_related('deptno','mgr')
    # for emp query
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(ename='SCOTT')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(sal__gt=2000)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno=20)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(hiredate='2025-3-13')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='M')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(ename__endswith='s')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(job='MANAGER')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(sal__lt=2000)

    # for dept query
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__deptno=30)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__deptno__range=(19,31))
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__in=('SALES','RESEARCH'))
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES',deptno=30  )
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__loc='CHICAGO')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__deptno__gt=19)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__loc='NEW YORK')
    
    # FOR MGR query
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno=10)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno=30)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__comm__isnull=False)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__job__in=('SALES','RESEARCH'))
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__job='SALES',deptno=30  )
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gt=2500)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno__gt=19)
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    QLEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__hiredate__gt='2024-1-1')

    d={'QLEDMO':QLEDMO}
    return render(request,'EmpToDeptAndMgr.html',d)

# prefetch_related join

def EmpToDeptByPR(request):
    QLDO=Dept.objects.prefetch_related('emp_set').all()
    QLDO=Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(ename='MARTIN')))

    d={'QLDO':QLDO}
    return render(request,'EmpToDeptByPR.html',d)


# update
def update_display(request):
    # using update method

    Emp.objects.filter(job='SALESMAN').update(sal=3500)
    Emp.objects.filter(ename='lucky').update(sal=3500)
    Emp.objects.filter(ename='KING').update(sal=5500)
    Emp.objects.filter(ename='SMITH').update(deptno=50)

    # using update_or_create method

    # Emp.objects.update_or_create(ename='BLAKE',defaults={'job':'ANALYST'})
    # Emp.objects.update_or_create(job='CLERK',defaults={'job':'ANALYST'})

    DO=Dept.objects.get(deptno=10)
    Emp.objects.update_or_create(ename='LUCKY',defaults={'hiredate':'2025-03-27','sal':2000,'deptno':DO})
    TEO=Emp.objects.all()
    d={'TEO':TEO}
    return render(request,'insert_emp.html',d)


# delete
def delete_display(request):
    Emp.objects.filter(ename='SMITH').delete()
    Emp.objects.filter(ename='JONES').delete()
    TEO=Emp.objects.all()
    d={'TEO':TEO}
    return render(request,'insert_emp.html',d)


