# Generated by Django 3.2.5 on 2022-02-09 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_threadmodel_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threadmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.user'),
        ),
    ]
