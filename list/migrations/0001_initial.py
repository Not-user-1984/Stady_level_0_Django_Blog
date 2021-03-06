# Generated by Django 4.0.5 on 2022-06-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(blank=True)),
                ('cried_ad', models.DateTimeField(auto_now_add=True)),
                ('upcried_ad', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('is_bulishen', models.BooleanField(default=True)),
            ],
        ),
    ]
