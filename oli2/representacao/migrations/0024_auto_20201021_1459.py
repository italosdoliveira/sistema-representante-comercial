# Generated by Django 2.2.6 on 2020-10-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0023_auto_20201021_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='imagem',
            field=models.CharField(max_length=600, null=True),
        ),
    ]