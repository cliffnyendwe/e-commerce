# Generated by Django 2.2 on 2020-08-09 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20200806_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderbags',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderbags',
            name='user',
        ),
        migrations.RemoveField(
            model_name='item',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='location',
        ),
        migrations.DeleteModel(
            name='Bags',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='OrderBags',
        ),
    ]
