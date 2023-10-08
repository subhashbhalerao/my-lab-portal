# Generated by Django 4.2.5 on 2023-09-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exp_Lists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('exp_no', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('dt', models.DateField()),
                ('file', models.FileField(upload_to='')),
                ('faculty', models.CharField(max_length=250)),
            ],
        ),
    ]