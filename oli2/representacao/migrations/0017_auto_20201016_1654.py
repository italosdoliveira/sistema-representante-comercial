# Generated by Django 2.2.6 on 2020-10-16 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0016_auto_20201016_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='id_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='representacao.Usuarios'),
        ),
        migrations.AlterField(
            model_name='prepostos',
            name='id_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='representacao.Usuarios'),
        ),
    ]
