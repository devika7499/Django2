# Generated by Django 4.2.1 on 2023-05-25 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_well_number', models.CharField(max_length=20)),
                ('oil', models.IntegerField()),
                ('gas', models.IntegerField()),
                ('brine', models.IntegerField()),
            ],
        ),
    ]
