# Generated by Django 3.1.5 on 2021-01-28 15:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Asset',
                'verbose_name_plural': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='Asset_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Asset_type',
                'verbose_name_plural': 'Assets_types',
            },
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=100)),
                ('asset_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.asset_type')),
            ],
            options={
                'verbose_name': 'Attribute',
                'verbose_name_plural': 'Attributes',
            },
        ),
        migrations.CreateModel(
            name='Attribute_value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Attribute_value',
                'verbose_name_plural': 'Attributes_values',
            },
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Control',
                'verbose_name_plural': 'Controls',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'System',
                'verbose_name_plural': 'Systems',
            },
        ),
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Threat',
                'verbose_name_plural': 'Threats',
            },
        ),
        migrations.CreateModel(
            name='Threat_has_control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.control')),
                ('threat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.threat')),
            ],
        ),
        migrations.CreateModel(
            name='Threat_has_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.attribute')),
                ('threat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.threat')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('xml', models.FileField(upload_to='processes/xml/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xml', 'bpmn'])])),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.system')),
            ],
            options={
                'verbose_name': 'Process',
                'verbose_name_plural': 'Processes',
            },
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.attribute_value'),
        ),
        migrations.CreateModel(
            name='Asset_has_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.asset')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.attribute')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.asset_type'),
        ),
        migrations.AddField(
            model_name='asset',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.process'),
        ),
    ]
