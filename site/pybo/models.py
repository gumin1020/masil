from django.db import models

# Create your models here.


class Member(models.Model):  # 회원
    mem_id = models.CharField(max_length=15, primary_key=True)  # 회원ID
    name = models.CharField(max_length=20)      # 이름
    phone = models.CharField(max_length=13)     # 연락처
    email = models.EmailField()     # 이메일
    address = models.TextField()    # 주소
    pw = models.CharField(max_length=15)    # 비밀번호
    pw_1 = models.CharField(max_length=15)  # 비밀번호 확인


class Thema(models.Model):      # 테마
    t_no = models.CharField(max_length=20, primary_key=True)    # 테마번호
    t_name = models.CharField(max_length=20)    # 테마이름


class Path(models.Model):   # 구간
    p_no = models.CharField(max_length=20, primary_key=True)    # 구간번호
    t_no = models.ForeignKey(Thema, on_delete=models.CASCADE, db_column='t_no')     # FK 테마-테마번호
    p_name = models.CharField(max_length=20)    # 구간이름
    position = models.TextField()   # 위치
    distance = models.CharField(max_length=10)  # 길이
    time = models.CharField(max_length=10)  # 시간


class Chat(models.Model):   # 채팅
    ch_no = models.CharField(max_length=30, primary_key=True)   # 채팅방번호
    ch_name = models.TextField()    # 채팅장명
    ch_to = models.CharField(max_length=10)     # 채팅자수
    mem_id = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='mem_id')    # FK 회원-회원ID


class Cotalk(models.Model):     # 코스게시판
    c_no = models.IntegerField(max_length=15, primary_key=True)     # 코스번호
    com = models.CharField(max_length=20)   # 커뮤니티 분류 - 불편사항, 추천
    b_title = models.CharField(max_length=40)   # 게시판(작성 글) 제목
    ct = models.TextField()     # 내용(작성 글 내용)
    img = models.ImageField(null=True)   # 이미지 - 첨부파일 / 이미지는 null 허용
    mem_id = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='mem_id')    # FK 회원-회원ID


class Comment(models.Model):    # 댓글
    com_no = models.CharField(max_length=30, primary_key=True)  # 댓글번호
    content = models.TextField()    # 댓글내용
    days = models.DateTimeField(max_length=30)  # 날짜
    mem_id = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='mem_id')    # FK 회원-회원ID
    c_no = models.ForeignKey(Cotalk, on_delete=models.CASCADE, db_column='c_no')    # FK 코스게시판 - 코스게시판 번호


class Us(models.Model):     # 동행 게시판
    us_no = models.CharField(max_length=5, primary_key=True)    # 동행번호 : 동행게시판 게시물 번호
    date = models.DateTimeField()   # 날짜(동행 일정)
    section = models.CharField(max_length=20)   # 구간
    p_num = models.CharField(max_length=2)  # 인원수
    mem_id = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='mem_id')    # FK 회원-회원ID






