# Generated by Django 3.2.18 on 2023-04-24 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_course_department'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
