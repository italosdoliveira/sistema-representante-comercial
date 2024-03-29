# Generated by Django 2.2.6 on 2020-11-23 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0055_auto_20201120_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinhaEmpresa',
            fields=[
                ('id_minha_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='minha-empresa/')),
                ('razao_social', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('nome_fantasia', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('cnpj', models.CharField(blank=True, db_index=True, max_length=25, null=True)),
                ('tipo_ie', models.CharField(choices=[('CONTRIBUINTE', 'CONTRIBUINTE'), ('NAO CONTRIBUINTE', 'NÃO CONTRIBUINTE'), ('ISENTO', 'ISENTO')], max_length=30, null=True)),
                ('inscricao_estadual', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('telefone', models.CharField(blank=True, max_length=80, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_nfe', models.EmailField(blank=True, max_length=254, null=True)),
                ('endereco', models.CharField(blank=True, max_length=80, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro', models.CharField(blank=True, max_length=80, null=True)),
                ('cep', models.CharField(blank=True, max_length=20, null=True)),
                ('cidade', models.CharField(blank=True, max_length=150, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='clientes',
            name='cnpj',
            field=models.CharField(db_index=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='inscricao_estadual',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nome_fantasia',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='razao_social',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contatos',
            name='nome_contato',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='cnpj',
            field=models.CharField(blank=True, db_index=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='inscricao_estadual',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='nome_fantasia',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='razao_social',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='data_entrega',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='data_pedido',
            field=models.DateField(db_index=True, default=datetime.date(2020, 11, 23), null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='numero_pedido',
            field=models.CharField(db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='ordem_compra',
            field=models.CharField(db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='codigo_produto',
            field=models.CharField(blank=True, db_index=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='descricao',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nome',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
    ]
