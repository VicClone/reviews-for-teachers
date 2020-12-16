# Generated by Django 2.2 on 2020-12-13 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_auto_20201213_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='student',
        ),
        migrations.AddField(
            model_name='reviews',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Groups', verbose_name='Группа'),
        ),
    ]