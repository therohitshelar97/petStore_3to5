# Generated by Django 5.0 on 2023-12-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='salary',
            field=models.FloatField(null=True),
        ),
    ]
