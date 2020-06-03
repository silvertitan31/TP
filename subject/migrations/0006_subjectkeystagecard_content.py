# Generated by Django 3.0.6 on 2020-05-30 20:39

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0005_auto_20200530_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectkeystagecard',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add Your Title', required=True)), ('text', wagtail.core.blocks.CharBlock(help_text='Add Additional Text', required=True))])), ('full_richtext', streams.blocks.RichTextBlock()), ('simple_richtext', streams.blocks.LimitedRichTextBlock())], blank=True, null=True),
        ),
    ]