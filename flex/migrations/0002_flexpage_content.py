# Generated by Django 3.0.6 on 2020-05-29 00:57

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add Your Title', required=True)), ('text', wagtail.core.blocks.CharBlock(help_text='Add Additional Text', required=True))]))], blank=True, null=True),
        ),
    ]