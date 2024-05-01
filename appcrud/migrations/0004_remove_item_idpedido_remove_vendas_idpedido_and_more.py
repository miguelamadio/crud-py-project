# Generated by Django 5.0.4 on 2024-05-01 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcrud', '0003_alter_pedido_idcliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='idPedido',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='idPedido',
        ),
        migrations.AddField(
            model_name='item',
            name='idVenda',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appcrud.vendas'),
        ),
        migrations.AlterField(
            model_name='item',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
