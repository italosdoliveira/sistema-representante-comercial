# Generated by Django 2.2.6 on 2020-12-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0061_remove_acompanhamentos_dias_trabalhados'),
    ]

    operations = [
        migrations.AddField(
            model_name='acompanhamentos',
            name='dias_trabalhados',
            field=models.IntegerField(default=0),
        ),
    ]
