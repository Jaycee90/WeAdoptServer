# Generated by Django 5.0.7 on 2024-07-23 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collected',
            name='currency',
            field=models.CharField(default='USD', max_length=50),
        ),
    ]
