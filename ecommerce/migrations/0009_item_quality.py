# Generated by Django 2.2 on 2019-10-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_auto_20191001_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quality',
            field=models.CharField(default='best', max_length=50),
        ),
    ]
