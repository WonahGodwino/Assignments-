# Generated by Django 4.1.2 on 2022-10-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artiste',
            name='age',
        ),
        migrations.AlterField(
            model_name='artiste',
            name='artiste_id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
