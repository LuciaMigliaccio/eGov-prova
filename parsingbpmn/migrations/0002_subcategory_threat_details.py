# Generated by Django 3.1.5 on 2021-01-28 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('function', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
            },
        ),
        migrations.CreateModel(
            name='Threat_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('threat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.threat')),
            ],
            options={
                'verbose_name': 'Threat_details',
                'verbose_name_plural': 'Threats_details',
            },
        ),
    ]
