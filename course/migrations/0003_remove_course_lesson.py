# Generated by Django 4.2.6 on 2023-10-31 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lesson',
        ),
    ]
