# Generated by Django 3.2.15 on 2022-08-11 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220811_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.IntegerField(choices=[(0, 'Beginner'), (1, 'Regular'), (2, 'Hard')], default=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='serves',
            field=models.IntegerField(choices=[(1, '1 Person'), (2, '2 People'), (3, '3 People'), (4, '4 People'), (5, '5 People'), (6, '6 People'), (7, '7 People'), (8, '8 People')], default=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_to_cook',
            field=models.IntegerField(choices=[(1, '5 Minutes'), (2, '10 Minutes'), (3, '15 Minutes'), (4, '20 Minutes'), (5, '25 Minutes'), (6, '30 Minutes'), (7, '40 Minutes'), (8, '50 Minutes'), (9, '60 Minutes')], default=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_to_prepare',
            field=models.IntegerField(choices=[(1, '5 Minutes'), (2, '10 Minutes'), (3, '15 Minutes'), (4, '20 Minutes'), (5, '25 Minutes'), (6, '30 Minutes'), (7, '40 Minutes'), (8, '50 Minutes'), (9, '60 Minutes')], default=1),
        ),
    ]
