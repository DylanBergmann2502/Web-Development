# Generated by Django 4.1.7 on 2023-04-03 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='default_pics/default_event.jpg', upload_to='event_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default_pics/default_post.jpg', upload_to='post_pics'),
        ),
    ]