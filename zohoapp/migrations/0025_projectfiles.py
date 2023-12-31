# Generated by Django 3.2.19 on 2023-09-30 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0024_alter_task_billdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(null=True, upload_to='doc/')),
                ('proj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.project1')),
            ],
        ),
    ]
