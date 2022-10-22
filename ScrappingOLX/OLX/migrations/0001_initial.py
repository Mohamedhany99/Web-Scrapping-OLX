# Generated by Django 4.0.5 on 2022-10-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(default='None', max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('price', models.FloatField()),
            ],
        ),
    ]
