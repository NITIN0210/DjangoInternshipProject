# Generated by Django 3.2.4 on 2021-07-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0002_auto_20210719_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='mails',
            name='senderid',
            field=models.CharField(default='a', max_length=10),
        ),
    ]
