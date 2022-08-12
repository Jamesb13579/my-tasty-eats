# Generated by Django 3.2.15 on 2022-08-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_recipe_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.IntegerField(choices=[('Beginner', 'Beginner'), ('Regular', 'Regular'), ('Hard', 'Hard')], default=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='serves',
            field=models.IntegerField(choices=[('1 Person', '1 Person'), ('2 People', '2 People'), ('3 People', '3 People'), ('4 People', '4 People'), ('5 People', '5 People'), ('6 People', '6 People'), ('7 People', '7 People'), ('8 People', '8 People')], default=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_to_cook',
            field=models.IntegerField(choices=[('5 Minutes', '5 Minutes'), ('10 Minutes', '10 Minutes'), ('15 Minutes', '15 Minutes'), ('20 Minutes', '20 Minutes'), ('25 Minutes', '25 Minutes'), ('30 Minutes', '30 Minutes'), ('40 Minutes', '40 Minutes'), ('50 Minutes', '50 Minutes'), ('60 Minutes', '60 Minutes')], default=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_to_prepare',
            field=models.IntegerField(choices=[('5 Minutes', '5 Minutes'), ('10 Minutes', '10 Minutes'), ('15 Minutes', '15 Minutes'), ('20 Minutes', '20 Minutes'), ('25 Minutes', '25 Minutes'), ('30 Minutes', '30 Minutes'), ('40 Minutes', '40 Minutes'), ('50 Minutes', '50 Minutes'), ('60 Minutes', '60 Minutes')], default=1),
        ),
    ]
