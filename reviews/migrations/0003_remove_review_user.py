# Generated by Django 3.1.3 on 2020-11-22 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]