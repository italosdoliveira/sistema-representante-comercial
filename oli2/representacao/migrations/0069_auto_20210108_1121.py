# Generated by Django 2.2.6 on 2021-01-08 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0068_remove_prepostos_possui_vinculo_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itenspedido',
            name='custo_unitario',
        ),
        migrations.RemoveField(
            model_name='itenspedido',
            name='custo_unitario_original',
        ),
    ]