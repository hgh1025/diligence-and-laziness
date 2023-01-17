from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def home(request):
    now_time=DateFormat(datetime.now()).format('Hi')
    go_time=request.POST.get('go_time')
    leave_time=request.POST.get('leave_time')
    
   
  
    work=Commute(go_time=go_time,leave_time=leave_time)
    work.save()
    
   
  
    return render(request, 'main/home.html')
    
def commute(request):
  users= User.objects.all()
  commutes = Commute.objects.all()
  go_time=DateFormat(datetime.now()).format('H:i')
  leave_time=request.POST.get('leave_time')
  # go_hour = commutes['go_time'].strftime('%Z')
  
  context = dict()
  context['commutes']=commutes
  context['users']=users
  context['go_time']=go_time
  # context['go_time']=go_time
  # context['leave_time']=leave_time
  return render(request, 'main/commute.html',context)
  
def mypage(request):

    commutes = Commute.objects.all()
    
    context = dict()
    
    
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
  schedules = Schedule.objects.all()

  if not 'user_email' in request.session.keys():
    return HttpResponse('로그인을 진행해 주세요')
  else:
    schedules = Schedule.objects.all()
    return render(request, 'main/calendar.html',{'schedules':schedules})


def schedules(request):
    
    
    schedule_content = request.POST.get('schedule_content')
    
    context = Schedule(schedule_content=schedule_content)
    
    context.save()
    print(schedule_content)
    print('hello')
    print(schedules)
    return redirect('main_calendar')
    
def login(request):
    
    loginEmail = request.POST['loginEmail'] # signin.html <input name=loginEmail> 사용을 위해
    loginPW = request.POST['loginPW']  # signin.html <input name=loginPW> 사용을 위해
    
    # 22/12/30 예외처리
    
    try:
        user = User.objects.get(user_email=loginEmail)
       

        if loginPW ==user.user_password and loginEmail==user.user_email:
            request.session['user_name'] = user.user_name
            request.session['user_email'] = user.user_email
            # message=messages.add_message(request,messages.ERROR,'로그인에 성공하였습니다') 
            
            return redirect('main_calendar')
        elif user.user_password != loginPW:
            message = '비밀번호를 틀렸습니다'
            return HttpResponse(message)
            
        else:
            return redirect('main_index')
    except ObjectDoesNotExist:   
        message = '이메일이 존재하지 않습니다.'
        return HttpResponse(message)
    except:
        message = '알 수 없는 오류가 발생했습니다..'
        return HttpResponse(message)    
    
def logout(request):
    del request.session['user_name']
    del request.session['user_email']
    return redirect('main_index')
