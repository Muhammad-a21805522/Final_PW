# Generated by Django 3.2.4 on 2021-06-22 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_resultadoquizz'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultadoquizz',
            name='resultado',
            field=models.IntegerField(default=0),
        ),
    ]