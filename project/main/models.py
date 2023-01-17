from django.db import models
from .models import*
# Create your models here.

class User(models.Model):
     
    user_email = models.EmailField(max_length= 20 ,unique=True) #회원아이디
    user_name = models.CharField(max_length= 20 ,primary_key=True) #회원이름
    user_date = models.DateTimeField(auto_now_add=True) #가입일(처음 등록한 시간으로 저장)
    user_password = models.CharField(max_length = 100) #회원 패스워드
    
    STATUS = (('남자','남자'), ('여자','여자'))
    gender = models.CharField(max_length=5 ,choices=STATUS , null=True) #성별
    age = models.IntegerField(null=True) # 나이
    year = models.IntegerField(null=True) 
    month= models.IntegerField( null=True)
    day= models.IntegerField(null=True)

    class Meta:
        db_table = 'user_tb'
        
    def __str__(self):
        return f'[{self.pk}] {self.user_name}'    

class Working_condition(models.Model):
    user_email=models.ForeignKey(User, to_field='user_email', related_name='work', on_delete = models.CASCADE, db_column="user_email", max_length= 20, null=True) #fk추가
    go = models.CharField(max_length= 20) #출근
    leave = models.CharField(max_length= 20) #퇴근
    vacation = models.CharField(max_length= 20) #휴가
    sick = models.CharField(max_length= 20) #병가
    holiday = models.CharField(max_length= 20) #대체휴일
    absence = models.CharField(max_length= 20) #결근
    half_vacation = models.CharField(max_length= 20) #반차
    travel = models.CharField(max_length= 20) #출장

    class Meta:
        db_table = 'working_tb' 
    
    def __str__(self):
        return f'[{self.pk}] {self.user_email}'
   

class Commute(models.Model):
    user_email=models.ForeignKey(User, to_field='user_email', related_name='commute', on_delete = models.CASCADE, db_column="user_email", max_length= 20, null=True) #fk추가
    current_time = models.DateTimeField(auto_now_add=True) #현재시간
    go_time = models.DateTimeField(auto_now_add=True) #출근시간
    leave_time = models.DateTimeField(auto_now_add=True) #퇴근시간
    total_time = models.IntegerField(null=True) #근무시간

  
    class Meta:
        db_table = 'commute_tb'
    
    def __str__(self):
        return f'[{self.pk}] {self.user_email}'
        
class Pay(models.Model):
    user_email=models.ForeignKey(User, to_field='user_email', related_name='pay', on_delete = models.CASCADE, db_column="user_email", max_length= 20, null=True) #fk추가
    overtime = models.IntegerField(null=True)#연장근무
    night = models.IntegerField(null=True)#야간근무
    weekend = models.IntegerField(null=True)#주말근무
    travel = models.IntegerField(null=True)#출장수당
    class Meta:
      db_table = 'pay_tb'
    def __str__(self):
        return f'[{self.pk}] {self.user_email}'
        
class Vacation(models.Model):
    user_email=models.ForeignKey(User, to_field='user_email', related_name='vacation_email', on_delete = models.CASCADE, db_column="user_email", max_length= 20, null=True) #fk추가
    user_name = models.ForeignKey(User, to_field='user_name', related_name='vacation_name', on_delete = models.CASCADE, db_column="user_name", max_length= 20, null=True) #fk추가
    total_vacation = models.IntegerField(null=True)  #총 휴가
    rest_vacation = models.IntegerField(null=True) # 잔여 휴가
    use_vacation = models.IntegerField(null=True) # 사용 휴가

    class Meta:
        db_table = 'vacation_tb'
    def __str__(self):
        return f'[{self.pk}] {self.user_email}'
        
class Schedule(models.Model):
    schedule_content = models.CharField(max_length= 100)
    user_email=models.ForeignKey(User, to_field='user_email', related_name='schedule', on_delete = models.CASCADE, db_column="user_email", max_length= 20, null=True) #fk추가
    
    def __str__(self):
        return f'[{self.pk}] {self.user_email}'