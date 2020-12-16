# Generated by Django 2.2 on 2020-12-13 07:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20201209_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='date',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='student',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='text',
        ),
        migrations.AddField(
            model_name='reviews',
            name='dateEnd',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата конца'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='dateStart',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата начала'),
        ),
        migrations.CreateModel(
            name='Сriterions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Сriterions', max_length=300, verbose_name='Название')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Reviews', verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Критерий',
                'verbose_name_plural': 'Критерии',
            },
        ),
        migrations.CreateModel(
            name='СriterionAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default='0', verbose_name='Оценка')),
                ('criterion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Сriterions', verbose_name='Критерий')),
            ],
            options={
                'verbose_name': 'Критерий ответ',
                'verbose_name_plural': 'Критерии ответ',
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('rating', models.PositiveIntegerField(default=0, verbose_name='Значение')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Students', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]