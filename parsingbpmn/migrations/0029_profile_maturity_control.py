# Generated by Django 3.1.5 on 2021-02-19 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0028_delete_profile_maturity_control'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile_maturity_control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.control')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.profile')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.subcategory')),
            ],
        ),
    ]
