# Generated by Django 3.2.6 on 2021-10-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keylib', '0002_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
