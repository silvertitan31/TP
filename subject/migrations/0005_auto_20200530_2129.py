# Generated by Django 3.0.6 on 2020-05-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0004_auto_20200530_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectkeystagecard',
            name='title',
            field=models.CharField(help_text='Enter the Key Stage Level', max_length=20, unique=True),
        ),
    ]
