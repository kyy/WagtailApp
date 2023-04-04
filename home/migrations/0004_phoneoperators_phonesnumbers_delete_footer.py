# Generated by Django 4.1.7 on 2023-04-04 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneOperators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(blank=True, choices=[('A1', 'A1.png'), ('MTС', 'MTС.png'), ('Life', 'Life.png'), ('City', 'City.png')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='PhonesNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=32, null=True)),
                ('operator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.phoneoperators')),
            ],
            options={
                'verbose_name': 'Футер',
                'verbose_name_plural': 'Футеры',
            },
        ),
        migrations.DeleteModel(
            name='Footer',
        ),
    ]
