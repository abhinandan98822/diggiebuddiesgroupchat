# Generated by Django 4.1.2 on 2022-11-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_filemodel_delete_msgfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='doc',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]