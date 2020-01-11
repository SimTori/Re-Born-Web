from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, user_id, password, email, hp, name, student_id, grade, department, circles, **extra_fields):
        if not user_id:
            raise ValueError('user_id Required!')

        user = self.model(
            user_id = user_id,
            email = email,
            hp = hp,
            name = name,
            student_id = student_id,
            grade = grade,
            department = department,
            circles = circles,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, email=None, hp=None, name=None, student_id=None, grade=None, department=None, circles=None):

        user = self.create_user(user_id, password, email, hp, name, student_id, grade)

        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    objects = UserManager()

    GRADE_CHOICES = (
        ("1학년", "1학년"),
        ("2학년", "2학년"),
        ("3학년", "3학년"),
        ("4학년", "4학년"),
        ("졸업생", "졸업생"),
    )

    LEVEL_CHOICES = (
        ("3", "Lv3_미인증사용자"),
        ("2", "Lv2_인증사용자"),
        ("1", "Lv1_관리자"),
        ("0", "Lv0_개발자"),
    )

    CIRCLES_CHOICES = (
        ("미가입", "미가입"),
        ("NUXPIA", "NUXPIA"),
        ("NET", "NET"),
        ("DOT-GABI", "DOT-GABI"),
        ("IMAGINE", "IMAGINE"),
        ("P&N", "P&N"),
        ("MEGA-BRAIN", "MEGA-BRAIN"),
    )

    DEPARTMENT_CHOICES = (
        ("외부인", "학부생이 아님"),
        ("컴퓨터공학부", "컴퓨터공학부"),
        ("드론IOT시뮬레이션학부", "드론IOT시뮬레이션학부"),
        ("의과대학", "의과대학"),
        ("문리과대학", "문리과대학"),
        ("사회과학대학", "사회과학대학"),
        ("공과대학", "공과대학"),
        ("보건의료융합대학", "보건의료융합대학"),
        ("BNIT융합대학", "BNIT융합대학"),
        ("약학대학", "약학대학"),
    )

    user_id = models.CharField(max_length=32, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    email = models.EmailField(max_length=128, verbose_name="이메일",null=True, unique=True)
    hp = models.IntegerField(verbose_name="핸드폰번호", null=True, unique=True)
    name = models.CharField(max_length=32, verbose_name="이름",null=True, unique=True)
    student_id = models.IntegerField(verbose_name="학번", null=True, unique=True)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=18, verbose_name="학년", null=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="등급", default=3)
    circles = models.CharField(choices=CIRCLES_CHOICES, max_length=18, verbose_name="동아리", null=True)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=24, verbose_name="학과", null=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "회원목록"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"