# Generated by Django 4.1.5 on 2023-03-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todomodel_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
