# Generated by Django 3.0.6 on 2020-05-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmpID', models.IntegerField(primary_key=True, serialize=False)),
                ('Empname', models.CharField(max_length=40)),
                ('EmpAge', models.IntegerField()),
                ('EmpSal', models.FloatField()),
                ('EmpDesignation', models.CharField(max_length=40)),
                ('Empcity', models.CharField(max_length=40)),
            ],
        ),
    ]
