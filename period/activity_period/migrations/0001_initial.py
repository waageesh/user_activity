# Generated by Django 3.0.5 on 2020-06-03 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='W012A3CDE', max_length=30)),
                ('real_name', models.CharField(default='JOHN DAVID', max_length=50)),
                ('tz', models.CharField(default='America/Los_Angeles', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(default='Feb 1 2020  1:33PM', max_length=50)),
                ('end_time', models.CharField(default='Feb 1 2020  1:33PM', max_length=50)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='activities', to='activity_period.User')),
            ],
        ),
    ]
