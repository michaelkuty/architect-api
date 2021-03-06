# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-03 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import yamlfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('engine', models.CharField(default='saltstack', max_length=32)),
                ('metadata', yamlfield.fields.YAMLField(blank=True, null=True)),
                ('status', models.CharField(default='unknown', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=32)),
                ('size', models.IntegerField(default=1)),
                ('metadata', yamlfield.fields.YAMLField(blank=True, null=True)),
                ('status', models.CharField(default='unknown', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('kind', models.CharField(max_length=32)),
                ('size', models.IntegerField(default=1)),
                ('metadata', yamlfield.fields.YAMLField(blank=True, null=True)),
                ('status', models.CharField(default='unknown', max_length=32)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Manager')),
            ],
        ),
        migrations.AddField(
            model_name='relationship',
            name='link_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_from', to='manager.Resource'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='link_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_to', to='manager.Resource'),
        ),
    ]
