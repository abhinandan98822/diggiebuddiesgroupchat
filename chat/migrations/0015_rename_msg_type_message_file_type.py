# Generated by Django 4.1.2 on 2022-11-22 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_alter_filemodel_doc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='msg_type',
            new_name='file_type',
        ),
    ]