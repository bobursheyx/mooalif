# Generated by Django 5.2 on 2025-04-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ariza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('xabar', models.TextField()),
            ],
        ),
    ]
