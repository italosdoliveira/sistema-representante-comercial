# Generated by Django 2.2.6 on 2020-10-23 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0031_auto_20201023_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='horario_pedido',
            field=models.TimeField(blank=True, default=datetime.time(9, 48, 11, 407036), null=True),
        ),
    ]