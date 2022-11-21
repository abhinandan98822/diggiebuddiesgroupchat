# Generated by Django 4.1.2 on 2022-11-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_alter_filemodel_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='media/')),
            ],
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='doc',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
