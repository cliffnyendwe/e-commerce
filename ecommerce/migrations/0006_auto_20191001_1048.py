# Generated by Django 2.2 on 2019-10-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20190930_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_status',
            field=models.CharField(choices=[('A', 'Available'), ('N', 'Not available'), ('R', 'Reserved')], max_length=1),
        ),
    ]
