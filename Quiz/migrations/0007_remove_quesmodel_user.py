# Generated by Django 4.1.5 on 2023-03-03 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_quesmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quesmodel',
            name='user',
        ),
    ]