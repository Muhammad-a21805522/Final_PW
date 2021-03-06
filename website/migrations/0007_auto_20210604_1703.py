# Generated by Django 3.2.4 on 2021-06-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_contacto_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clareza', models.IntegerField(default=50)),
                ('rigor', models.IntegerField(default=50)),
                ('precisao', models.IntegerField(default=50)),
                ('profundidade', models.IntegerField(default=50)),
                ('amplitude', models.IntegerField(default=50)),
                ('logica', models.IntegerField(default=50)),
                ('significancia', models.IntegerField(default=50)),
                ('originalidade', models.IntegerField(default=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefone',
            field=models.IntegerField(default=911524513),
        ),
    ]
