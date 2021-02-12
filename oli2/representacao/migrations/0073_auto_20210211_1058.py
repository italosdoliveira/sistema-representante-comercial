# Generated by Django 2.2.6 on 2021-02-11 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0072_auto_20210210_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefas',
            name='data_incial',
        ),
        migrations.AddField(
            model_name='tarefas',
            name='data_inicial',
            field=models.DateField(default=datetime.date(2021, 2, 11)),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='data_pedido',
            field=models.DateField(db_index=True, default=datetime.date(2021, 2, 11)),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='horario_pedido',
            field=models.TimeField(blank=True, default=datetime.time(10, 56, 32, 593812)),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='data_final',
            field=models.DateField(blank=True, default=datetime.date(2021, 2, 11), null=True),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='descricao_tarefa',
            field=models.CharField(max_length=800),
        ),
    ]