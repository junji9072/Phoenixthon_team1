from django.contrib.auth.models import AbstractUser
from datetime import datetime,timedelta,date
from django.db import models

# Create your models here.
class Users(AbstractUser):
  """Custom User Model"""

  USERTYPE_SOLDIER = "soldier"
  USERTYPE_CIVIL = "civil"

  USERTYPE_CHOICES = (
    (USERTYPE_SOLDIER, "soldier"),
    (USERTYPE_CIVIL, "civil"),
  )

  GENDER_MALE = "male"
  GENDER_FEMALE = "female"
  GENDER_OTHER = "other"

  GENDER_CHOICES = (
    (GENDER_MALE, "Male"), 
    (GENDER_FEMALE, "Female"),
    (GENDER_OTHER, "Other"),
  )
  usertype = models.CharField(max_length=10,choices=USERTYPE_CHOICES)
  name = models.CharField(max_length=30, blank=True)
  gender = models.CharField(choices=GENDER_CHOICES, max_length=7, blank=True) #성별
  phone_number = models.CharField(max_length=30, default=" ") #핸드폰 번호
  city = models.CharField(max_length = 50, blank = True, default = " ") #거주지

  class meta:
        abstract = True


class Soldier_User(Users):
  """Soldier User Model"""

  MILITARY_ARIFORCE = "공군" #공군
  MILITARY_ARMY = "육군" #육군
  MILITARY_NAVY = "해군" #해군
  MILITARY_MARIN = "해병대" #해병대
  MILITARY_OTHER = "기타" #기타

  MILITARY_CHOICES = (
    (MILITARY_ARIFORCE, "공군"),
    (MILITARY_ARMY, "육군"),  
    (MILITARY_NAVY, "해군"),
    (MILITARY_MARIN, "해병대"),
    (MILITARY_OTHER, "기타"),
  )

  # RANK_RECRUIT = "훈련병"
  # RANK_PRIVATE = "이병"
  # RANK_FIRSTCLASS = "일병"
  # RANK_SPECIALLIST = "상병"
  # RANK_SERGEANT = "병장"

  # RANK_CHOICES = (
  #   (RANK_RECRUIT,"훈련병"),
  #   (RANK_PRIVATE,"이병"),
  #   (RANK_FIRSTCLASS,"일병"),
  #   (RANK_SPECIALLIST,"상병"),
  #   (RANK_SERGEANT,"병장")
  # )

  devision = models.CharField(max_length=30) #소속 사단
  military_type = models.CharField(choices=MILITARY_CHOICES, max_length=12) #육해공
  enter_date = models.DateField(default = date.today) #입대일
  #rank = models.CharField(choices=RANK_CHOICES,max_length=15) #계급

  class Meta:
    verbose_name = "Soldier User"

  def get_leave_day(self): #전역일 계산하는 함수
    enter_day = str(self.enter_date).split("-")
    
    if(self.military_type=="육군"):
      period = 540
    elif(self.military_type=="해군"):
      period = 600
    elif(self.military_type=="공군"):
      period = 660
    elif(self.military_type=="해병대"):
      period = 540
    else:
      period = 1

    time1 = datetime(int(enter_day[0]),int(enter_day[1]),int(enter_day[2]))

    day = time1 + timedelta(days=period)

    return day

  def print_leave_day(self): #계산한 전역 일을 동일한 출력 형식으로 바꿔주는 함수
    day = str(self.get_leave_day())
    day = day.split("-")
    day2 = day[2].split(" ")
    day_format = day[0] + "-" + day[1] + "-"  + day2[0]
    return day_format

  def get_d_day(self): #남은 복무 날자 구하는 함수
    now = datetime.now()
    leave_day = self.get_leave_day()

    day = (leave_day-now).days
    return day

  def get_rank(self):
    days_left = self.get_d_day()
    if days_left<0:
      rank = "전역"
    elif days_left<150:
      rank = "병장"
    elif days_left<300:
      rank = "상병"
    elif days_left<450:
      rank = "일병"
    else:
      rank = "이등병"
    return rank


class Civil_User(Users):
  my_soldier = models.ManyToManyField(Soldier_User,blank=True)

  class Meta:
    verbose_name = "Civil User"
