# Generated by Django 4.2.18 on 2025-01-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstracao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='porcentagem_comissao',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_banheiro',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_cozinha',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_minimo',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_outros',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_quarto',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_quintal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_sala',
            field=models.FloatField(),
        ),
    ]