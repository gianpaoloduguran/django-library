# Generated by Django 4.1.3 on 2022-11-16 18:28

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('books', '0014_rename_author_tags_books_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
