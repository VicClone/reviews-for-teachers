# Generated by Django 2.2 on 2020-12-04 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20201106_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Organizer', verbose_name='Организатор'),
        ),
    ]
