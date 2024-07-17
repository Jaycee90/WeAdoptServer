# Generated by Django 5.0.7 on 2024-07-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0005_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
