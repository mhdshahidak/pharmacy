# Generated by Django 4.0.3 on 2022-04-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('puchase_cost', models.FloatField()),
                ('selling_cost', models.FloatField()),
            ],
            options={
                'db_table': 'medicine',
            },
        ),
    ]
