# Generated by Django 2.2 on 2020-12-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_reviews_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='сriterions',
            name='review',
        ),
        migrations.AddField(
            model_name='reviews',
            name='сriterions',
            field=models.ManyToManyField(related_name='сriterions', to='reviews.Сriterions', verbose_name='Критерии'),
        ),
    ]
