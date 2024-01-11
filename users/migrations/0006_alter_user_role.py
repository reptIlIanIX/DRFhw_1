# Generated by Django 4.2.6 on 2023-11-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'member'), ('moderator', 'moderator')], default='member', max_length=11),
        ),
    ]