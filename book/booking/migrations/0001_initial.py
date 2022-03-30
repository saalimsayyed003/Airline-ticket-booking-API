# Generated by Django 4.0.3 on 2022-03-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('To', models.CharField(blank=True, max_length=50)),
                ('From', models.CharField(blank=True, max_length=50)),
                ('Departure_date', models.DateField(blank=True)),
                ('Return_date', models.DateField(blank=True)),
                ('Class', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]