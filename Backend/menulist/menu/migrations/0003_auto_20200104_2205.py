# Generated by Django 3.0.2 on 2020-01-04 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200104_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='menu',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu',
            field=models.ManyToManyField(help_text="The menus that this category belongs to, i.e. 'Lunch'.", related_name='_menuitem_menu_+', to='menu.Menu'),
        ),
    ]
