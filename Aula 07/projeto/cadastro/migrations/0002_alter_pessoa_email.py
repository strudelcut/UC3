# Generated by Django 5.1.4 on 2025-01-07 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
