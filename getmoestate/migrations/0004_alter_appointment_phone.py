# Generated by Django 5.1.7 on 2025-03-14 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getmoestate', '0003_remove_appointment_agent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
