# Generated by Django 4.0.4 on 2022-06-05 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0003_menuitem_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_label',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='links', to='menu_app.menu'),
        ),
    ]
