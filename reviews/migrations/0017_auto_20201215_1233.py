# Generated by Django 2.2 on 2020-12-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0016_auto_20201214_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='availability',
            field=models.PositiveIntegerField(default=0, verbose_name='Доступность и понятность изложения материала'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='fascination',
            field=models.PositiveIntegerField(default=0, verbose_name='Увлекательность изложения материала'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='interest',
            field=models.PositiveIntegerField(default=0, verbose_name='Заинтересованность предметом'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='novelty',
            field=models.PositiveIntegerField(default=0, verbose_name='Новизна изученного материала'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='сomplexity',
            field=models.PositiveIntegerField(default=0, verbose_name='Сложность изученного материала'),
        ),
    ]
