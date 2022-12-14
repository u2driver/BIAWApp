# Generated by Django 4.1.3 on 2022-12-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invnumber', models.IntegerField()),
                ('category', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=225)),
                ('condition', models.CharField(max_length=225)),
                ('checkedout', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('zip', models.IntegerField()),
                ('date_out', models.DateField()),
                ('date_in', models.DateField(blank=True, null=True)),
                ('equip_id', models.IntegerField()),
            ],
        ),
    ]
