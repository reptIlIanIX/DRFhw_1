# Generated by Django 4.2.6 on 2023-11-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_managers_rename_name_user_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='name'),
        ),
    ]
