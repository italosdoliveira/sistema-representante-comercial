# Generated by Django 2.2.6 on 2021-02-12 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0076_auto_20210212_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='razao_social',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='horario_pedido',
            field=models.TimeField(blank=True, default=datetime.time(11, 24, 17, 718745)),
        ),
    ]