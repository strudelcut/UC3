# Generated by Django 5.1.4 on 2025-01-20 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tema', models.CharField(max_length=30)),
                ('foto', models.ImageField(upload_to='')),
                ('conteudo', models.TextField(blank=True, null=True)),
            ],
        ),
    ]