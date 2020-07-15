# Generated by Django 2.2.13 on 2020-07-15 17:45

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20200714_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]