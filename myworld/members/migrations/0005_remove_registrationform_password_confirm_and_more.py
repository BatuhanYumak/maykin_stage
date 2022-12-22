# Generated by Django 4.1.1 on 2022-12-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_registrationform_email_registrationform_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationform',
            name='password_confirm',
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='email',
            field=models.EmailField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='password',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='username',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
