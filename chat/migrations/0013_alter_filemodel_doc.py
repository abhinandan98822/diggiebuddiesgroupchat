# Generated by Django 4.1.2 on 2022-11-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='doc',
            field=models.FileField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]