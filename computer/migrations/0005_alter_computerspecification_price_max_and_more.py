# Generated by Django 4.0.2 on 2022-03-01 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0004_alter_computerspecification_price_max_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computerspecification',
            name='price_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='computerspecification',
            name='price_min',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='computerspecification',
            name='ram',
            field=models.IntegerField(default=0),
        ),
    ]
