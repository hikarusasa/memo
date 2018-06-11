# Generated by Django 2.0.6 on 2018-06-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='category',
        ),
        migrations.AddField(
            model_name='description',
            name='category',
            field=models.ManyToManyField(to='app.Category', verbose_name='カテゴリ'),
        ),
    ]