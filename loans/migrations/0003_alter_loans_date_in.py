# Generated by Django 4.1.3 on 2022-12-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_alter_loans_date_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='date_in',
            field=models.DateField(null=True),
        ),
    ]
