# Generated by Django 2.0.6 on 2020-11-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_lessons_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='name',
            field=models.CharField(default='review', max_length=150, verbose_name='Первый отзыв'),
        ),
    ]
