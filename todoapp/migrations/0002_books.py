# Generated by Django 3.1.6 on 2021-05-31 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('B_Name', models.CharField(max_length=200)),
                ('B_Author', models.CharField(max_length=150)),
                ('B_price', models.IntegerField()),
            ],
        ),
    ]
