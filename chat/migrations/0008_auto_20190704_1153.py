# Generated by Django 2.2.3 on 2019-07-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20190704_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='standardized_conviction_score',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
    ]