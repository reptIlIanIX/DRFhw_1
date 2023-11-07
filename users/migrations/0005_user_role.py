# Generated by Django 4.2.6 on 2023-11-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'member'), ('moderator', 'moderator')], default='member', max_length=9),
        ),
    ]
