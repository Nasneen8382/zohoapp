# Generated by Django 3.2.19 on 2023-09-30 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0022_auto_20230930_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='project1',
            name='end',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project1',
            name='start',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='billdate',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
    ]
