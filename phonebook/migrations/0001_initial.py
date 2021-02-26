# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('이름', models.CharField(max_length=50)),
                ('전화번호', models.CharField(max_length=20)),
                ('이메일', models.EmailField(max_length=254)),
                ('주소', models.CharField(max_length=100)),
                ('생년월일', models.DateField()),
            ],
        ),
    ]
