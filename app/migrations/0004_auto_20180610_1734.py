# Generated by Django 2.0.6 on 2018-06-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180610_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='category',
            field=models.ForeignKey(default='スポーツ', on_delete=True, to='app.Category', verbose_name='カテゴリ'),
        ),
    ]
