# Generated by Django 2.2 on 2020-12-13 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20201213_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Teachers', verbose_name='Преподаватель'),
        ),
    ]
