# Generated by Django 4.1.7 on 2023-05-04 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studenst', '0003_student_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='amount',
            new_name='price',
        ),
    ]
