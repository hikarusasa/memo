# Generated by Django 2.0.6 on 2018-06-10 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180610_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='app.Category', verbose_name='カテゴリ'),
        ),
    ]