# Generated by Django 3.1.6 on 2021-02-03 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.CharField(max_length=20)),
                ('wpts', models.IntegerField()),
                ('loser', models.CharField(max_length=20)),
                ('lpts', models.IntegerField()),
            ],
        ),
    ]