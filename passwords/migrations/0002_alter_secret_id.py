# Generated by Django 3.2.4 on 2021-11-14 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]
