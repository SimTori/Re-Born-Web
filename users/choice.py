# users APP choiceField
GRADE_CHOICES = (
    ("선택안함", "선택안함"),
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
    ("선택안함", "선택안함"),
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


# free APP choiceField
CATEGORY_CHOICES = (
    ("자유", "자유"),
    ("질문", "질문"),
    ("정보", "정보"),
)


# timetable APP choiceField
TIME_CHOICE = (
    ('1', '1교시(오전9시)'),
    ('2', '2교시(오전10시)'),
    ('3', '3교시(오전11시)'),
    ('4', '4교시(오후12시)'),
    ('5', '5교시(오후1시)'),
    ('6', '6교시(오후2시)'),
    ('7', '7교시(오후3시)'),
    ('8', '8교시(오후4시)'),
    ('9', '9교시(오후5시)'),
    ('10', '10교시(오후6시)'),
    ('11', '11교시(오후7시)'),
    ('12', '12교시(오후8시)'),
)

TIME_LENGTH_CHOICE = (
    ('1', '1시간'),
    ('2', '2시간'),
    ('3', '3시간'),
    ('4', '4시간'),
)

DAY_CHOICE = (
    ('mon', '월요일'),
    ('tue', '화요일'),
    ('wed', '수요일'),
    ('thu', '목요일'),
    ('fri', '금요일'),
    ('sat', '토요일'),
    ('sun', '일요일'),
)

SUBJECT_GRADE_CHOICE = (
    ("first", "1학년"),
    ("second", "2학년"),
    ("third", "3학년"),
    ("fourth", "4학년"),
)


# about APP choiceField
RANK_CHOICES = (
    ("1", "회장"),
    ("2", "부회장"),
    ("3", "부장"),
    ("4", "차장"),
    ("5", "부원"),
)


PART_CHOICES = (
    ("회장단", "회장단"),
    ("개발부", "개발부"),
    ("학술부", "학술부"),
    ("운영부", "운영부"),
    ("홍보부", "홍보부"),
    ("재정부", "재정부"),
)