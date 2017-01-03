# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-03 02:02
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0004_auto_20160426_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(blank=True, help_text=b'email', max_length=300, verbose_name=b'Mensagem Opcional'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='to_user',
            field=models.ForeignKey(help_text=b'Please invite', on_delete=django.db.models.deletion.CASCADE, related_name='invitations_received', to=settings.AUTH_USER_MODEL, verbose_name=b'invtations received'),
        ),
        migrations.AlterField(
            model_name='move',
            name='x',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='move',
            name='y',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
