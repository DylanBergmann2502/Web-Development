# Generated by Django 4.1.1 on 2022-11-22 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_room_participants_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]