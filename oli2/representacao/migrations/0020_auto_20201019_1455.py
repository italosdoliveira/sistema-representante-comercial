# Generated by Django 2.2.6 on 2020-10-19 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0019_pedidos_id_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='id_empresa_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fk_empresa_cliente', to='representacao.Clientes'),
        ),
    ]
