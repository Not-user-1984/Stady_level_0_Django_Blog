# Generated by Django 4.0.5 on 2022-06-22 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['upcried_ad'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='list',
            name='content',
            field=models.TextField(blank=True, verbose_name='контент'),
        ),
        migrations.AlterField(
            model_name='list',
            name='cried_ad',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='list',
            name='is_bulishen',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='list',
            name='photo',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='list',
            name='upcried_ad',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
        migrations.AddField(
            model_name='list',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='list.category'),
        ),
    ]
