# Generated by Django 5.0 on 2023-12-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datatables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatable',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datatable',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
    ]