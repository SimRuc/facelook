# Generated by Django 3.2.5 on 2022-01-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220129_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='body',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
