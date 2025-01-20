# Generated by Django 4.2.18 on 2025-01-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstracao', '0002_alter_servico_porcentagem_comissao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='porcentagem_comissao',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_banheiro',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_cozinha',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_minimo',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_outros',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_quarto',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_quintal',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_sala',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
