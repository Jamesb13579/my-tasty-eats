# Generated by Django 3.2.15 on 2022-08-08 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='serves',
            field=models.IntegerField(choices=[(1, '1 Person'), (2, '2 Person'), (3, '3 Person'), (4, '4 Person'), (5, '5 Person'), (6, '6 Person'), (7, '7 Person'), (8, '8 Person')], default=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_to_cook',
            field=models.IntegerField(choices=[(1, '5 MINUTES'), (2, '10 MINUTES'), (3, '15 MINUTES'), (4, '20 MINUTES'), (5, '25 MINUTES'), (6, '30 MINUTES'), (7, '40 MINUTES'), (8, '50 MINUTES'), (9, '60 MINUTES')], default=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_to_prepare',
            field=models.IntegerField(choices=[(1, '5 MINUTES'), (2, '10 MINUTES'), (3, '15 MINUTES'), (4, '20 MINUTES'), (5, '25 MINUTES'), (6, '30 MINUTES'), (7, '40 MINUTES'), (8, '50 MINUTES'), (9, '60 MINUTES')], default=1),
        ),
    ]
