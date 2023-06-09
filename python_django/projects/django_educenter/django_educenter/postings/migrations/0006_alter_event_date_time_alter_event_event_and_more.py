# Generated by Django 4.1.7 on 2023-04-05 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_myuser_email_alter_myuser_full_name_and_more'),
        ('postings', '0005_alter_event_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(verbose_name='Date & Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event',
            field=models.CharField(max_length=120, verbose_name='Event Name'),
        ),
        migrations.AlterField(
            model_name='event',
            name='speaker',
            field=models.ManyToManyField(to='users.teacher', verbose_name='Speakers'),
        ),
    ]
