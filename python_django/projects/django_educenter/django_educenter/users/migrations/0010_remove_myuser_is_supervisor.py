# Generated by Django 4.1.7 on 2023-04-01 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_teacher_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_supervisor',
        ),
    ]
