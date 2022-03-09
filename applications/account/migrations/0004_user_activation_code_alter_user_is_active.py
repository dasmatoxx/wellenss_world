# Generated by Django 4.0.2 on 2022-03-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_user_activation_code_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_code',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
