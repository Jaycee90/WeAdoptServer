# Generated by Django 5.0.7 on 2024-07-16 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='available',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
