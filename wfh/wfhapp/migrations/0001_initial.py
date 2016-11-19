# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-18 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WFH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onDate', models.DateField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(blank=True, default='<WFH:Today>', max_length=150)),
                ('tasks', models.TextField()),
                ('comments', models.CharField(blank=True, max_length=120)),
                ('teamMember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.TeamMember')),
            ],
            options={
                'ordering': ['teamMember', '-onDate'],
            },
        ),
    ]
