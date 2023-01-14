from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def mypage(request):
    commutes = Commute.objects.all()
    now = str(datetime.now().year) + "년"+ str(datetime.now().month )+ "월" 
    edit_time = str(datetime.now().year) + "."+ str(datetime.now().month)
    dd = str(datetime.now().day)
    context = dict()
    context['now'] = now
    context['edit_time'] = edit_time
    context['dd'] = dd
    context['commutes'] = commutes
    return render(request, 'main/mypage.html',context)

def join(request):
    

# 회원가입 start
    
  name = request.POST['signupName']
  email = request.POST['signupEmail']
  pw = request.POST['signupPW']
  gender= request.POST['gender']
    #year()로 하면 'int' object is not callable 에라가 나옴. 
    # 이유->예약어year(),sum()등등으로 변수명으로 했기때문에
  now=int(datetime.now().year)
  age= request.POST['year']
  age1= int(age)
  
  # 만 나이 구하기
  real_age = now - age1 + 1  
  #생년,월,일 
  year = request.POST.get('year')
  month = request.POST.get('month', False)
  day = request.POST.get('day', False)
   
  user = User(user_name = name, user_email = email, user_password = pw,
  gender=gender,age=real_age,year=year,month=month,day=day)
  user.save()
 # 회원가입 end
  
    
  return redirect('main_index' )

def calendar(request):
  
  return render(request, 'main/calendar.html')


def schedules(request):
    
    return render(request, 'main/calendar.html')
    
def logout(request):
    del request.session['user_name']
    del request.session['user_email']
    return redirect('main_signin')
