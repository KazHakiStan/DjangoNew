# Generated by Django 4.0.4 on 2022-06-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_post_options_post_created_at_post_is_public_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинки'),
        ),
    ]