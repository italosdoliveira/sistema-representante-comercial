# Generated by Django 2.2.6 on 2020-11-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('representacao', '0046_auto_20201106_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='C:/empresas'),
        ),
    ]
