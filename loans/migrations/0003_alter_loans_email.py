# Generated by Django 4.1.3 on 2023-06-16 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_loans_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]