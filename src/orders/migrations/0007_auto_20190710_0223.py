# Generated by Django 2.2.2 on 2019-07-10 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20190705_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded'), ('created', 'Created')], default='created', max_length=120),
        ),
    ]
