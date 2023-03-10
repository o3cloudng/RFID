# Generated by Django 4.1.7 on 2023-02-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=255, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='member',
            name='parent_guardian',
            field=models.CharField(max_length=200, verbose_name='Parent or Guardian name'),
        ),
    ]
