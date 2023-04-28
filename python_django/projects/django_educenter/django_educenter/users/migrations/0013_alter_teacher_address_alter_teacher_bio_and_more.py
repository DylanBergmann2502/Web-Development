# Generated by Django 4.1.7 on 2023-04-05 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_myuser_email_alter_myuser_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, default='default_pics/default_teacher.jpg', null=True, upload_to='teacher_pics'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]