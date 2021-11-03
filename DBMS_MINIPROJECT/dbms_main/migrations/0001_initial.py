# Generated by Django 3.1.7 on 2021-11-03 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_profile',
            fields=[
                ('stud_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('section', models.IntegerField()),
                ('roll_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='teacher_profile',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=500)),
                ('department', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbms_main.student_profile')),
            ],
        ),
        migrations.CreateModel(
            name='answer',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=500)),
                ('qid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbms_main.question')),
                ('solve_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbms_main.teacher_profile')),
            ],
        ),
    ]
