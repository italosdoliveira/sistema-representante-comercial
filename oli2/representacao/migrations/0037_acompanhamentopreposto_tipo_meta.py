# Generated by Django 2.2.6 on 2020-10-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0036_auto_20201028_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='acompanhamentopreposto',
            name='tipo_meta',
            field=models.CharField(choices=[('VALOR', 'VALOR'), ('PORCENTAGEM', 'PORCENTAGEM')], max_length=30, null=True),
        ),
    ]