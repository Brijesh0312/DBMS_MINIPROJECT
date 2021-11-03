from django.db import models

# Create your models here.
class student_profile(models.Model):
    stud_id= models.AutoField( primary_key=True)
    name=  models.CharField(max_length=30,)
    section=models.IntegerField()
    roll_no=models.IntegerField()
    email= models.EmailField(max_length = 254)
class teacher_profile(models.Model):
    teacher_id=models.AutoField( primary_key=True)
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
class question(models.Model):
    qid=models.AutoField( primary_key=True)
    description= models.TextField(max_length=500)
    department=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    stud_id=models.ForeignKey('student_profile', on_delete=models.CASCADE)
class answer(models.Model):
    aid=models.AutoField( primary_key=True)
    qid=models.ForeignKey('question', on_delete=models.CASCADE)
    description= models.TextField(max_length=500)
    solve_by=models.ForeignKey('teacher_profile', on_delete=models.CASCADE)