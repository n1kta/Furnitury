# Generated by Django 3.0.5 on 2020-07-06 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20200706_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mincategory',
            name='category',
        ),
        migrations.AddField(
            model_name='mincategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Category'),
        ),
    ]
