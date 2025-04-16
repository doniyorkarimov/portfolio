# Generated by Django 5.1.7 on 2025-03-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.CharField(blank=True, help_text='Client, e.g., Google', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='service',
            field=models.CharField(blank=True, help_text='Service, e.g., Web Development', max_length=100, null=True),
        ),
    ]
