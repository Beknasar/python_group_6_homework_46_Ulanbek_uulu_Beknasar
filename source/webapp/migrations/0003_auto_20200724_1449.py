# Generated by Django 2.2 on 2020-07-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200724_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_deadline',
            field=models.DateField(blank=True, default='0000-00-00', null=True, verbose_name='Дата выполнения'),
        ),
    ]