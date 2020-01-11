# Generated by Django 3.0.2 on 2020-01-04 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the item on the menu.', max_length=48)),
                ('description', models.CharField(blank=True, help_text='The description is a simple text description of the menu item.', max_length=128, null=True)),
                ('order', models.IntegerField(default=0, help_text='The order is to specify the order in which items show up on the menu.', verbose_name='order')),
                ('price', models.IntegerField(help_text='The price is the cost of the item.')),
                ('classification', models.CharField(choices=[('neither', 'Neither'), ('vegan', 'Vegan'), ('vegetarian', 'Vegetarian')], default=0, help_text='Select if this item classifies as Vegetarian, Vegan, or Neither.', max_length=10, verbose_name='classification')),
                ('spicy', models.BooleanField(default=False, help_text='Is this item spicy?', verbose_name='spicy?')),
                ('contains_peanuts', models.BooleanField(default=True, help_text='Does this item contain peanuts?', verbose_name='contain peanuts?')),
                ('gluten_free', models.BooleanField(default=False, help_text='Is this item Gluten Free?', verbose_name='gluten free?')),
            ],
            options={
                'verbose_name': 'menu item',
                'verbose_name_plural': 'menu items',
                'ordering': ['classification', 'order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='MenuCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='menu category name')),
                ('additional_text', models.CharField(blank=True, help_text="The additional text is any bit of related information to go along with a menu category, i.e. the 'Pasta' category might have details that say 'All entrees come with salad and bread'.", max_length=128, null=True)),
                ('order', models.IntegerField(default=0, help_text='The order is the order that this category should appear in when rendered on the templates.')),
                ('menu', models.ManyToManyField(help_text="The menus that this category belongs to, i.e. 'Lunch'.", related_name='_menucat_menu_+', to='menu.MenuItem')),
            ],
            options={
                'verbose_name': 'menu category',
                'verbose_name_plural': 'menu categories',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, unique=True, verbose_name='menu name')),
                ('additional_text', models.CharField(blank=True, help_text='Any additional text that the menu might need, i.e. Served between 11:00am and 4:00pm.', max_length=128, null=True)),
                ('order', models.PositiveSmallIntegerField(default=0, help_text='The order of the menu determines where this menu appears alongside other menus.')),
                ('category', models.ForeignKey(help_text="Category is the menu category that this menu item belongs to, i.e. 'Appetizers'.", on_delete=django.db.models.deletion.CASCADE, related_name='+', to='menu.MenuCat', verbose_name='menu category')),
            ],
            options={
                'ordering': ['name', 'order'],
            },
        ),
    ]