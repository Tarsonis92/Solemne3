# Generated by Django 2.1.2 on 2018-11-24 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_persona_constraseña'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='email',
            field=models.EmailField(default='usuario@usa.cl', max_length=254),
        ),
    ]
