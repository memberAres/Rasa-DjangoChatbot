# Generated by Django 2.2.3 on 2019-07-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20190704_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_db', models.CharField(max_length=80)),
                ('isin', models.CharField(max_length=80)),
                ('exchange', models.CharField(max_length=80)),
                ('bloomberg_id', models.CharField(max_length=80)),
                ('reuters_id', models.CharField(max_length=80)),
            ],
        ),
    ]
