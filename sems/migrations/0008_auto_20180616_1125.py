# Generated by Django 2.0.4 on 2018-06-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sems', '0007_afatet_provimeve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afatet_provimeve',
            name='muaji',
        ),
        migrations.AlterField(
            model_name='afatet_provimeve',
            name='deri',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='afatet_provimeve',
            name='prej',
            field=models.DateField(),
        ),
    ]
