# Generated by Django 2.2.6 on 2020-10-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0022_auto_20201021_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='aliquota',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='comissao',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='custo_unitario',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='dun',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='ean',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='ipi',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='multiplo',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='mva_st',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='pis',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='preco_embalagem',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='quantidade_embalagem',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='reducao_icms',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='st',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='validade',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
