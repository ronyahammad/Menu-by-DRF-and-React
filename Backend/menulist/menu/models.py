
from django.db import models

class MenuItem(models.Model):
	
	menu_category = models.ManyToManyField('MenuCategory', related_name='menuitem',help_text='The menus that this category belongs to, i.e. \'Lunch\'.') 
	name = models.CharField(max_length=48, help_text='Name of the item on the menu.')
	description = models.CharField(max_length=128, null=True, blank=True, help_text='The description is a simple text description of the menu item.')
	order = models.IntegerField(default=0, verbose_name='order', help_text='The order is to specify the order in which items show up on the menu.')
	price = models.FloatField(help_text='The price is the cost of the item.')
	#image = models.ImageField(upload_to='menu', null=True, blank=True, verbose_name='image', help_text='The image is an optional field that is associated with each menu item.')
	#menu_category = models.ForeignKey('self',on_delete=models.CASCADE, verbose_name='menu category', related_name='+', help_text='Category is the menu category that this menu item belongs to, i.e. \'Appetizers\'.')

	
	class Meta:
		ordering = ['order', 'name']

	def __unicode__(self):
		return self.name


class MenuCategory(models.Model):
	menu = models.ManyToManyField('Menu', related_name='menucategory',help_text='The menus that this category belongs to, i.e. \'Lunch\'.') 
	name = models.CharField(max_length=48, help_text='Name of the item on the menu.')
	description = models.CharField(max_length=128, null=True, blank=True, help_text='The description is a simple text description of the menu item.')
	order = models.IntegerField(default=0, verbose_name='order', help_text='The order is to specify the order in which items show up on the menu.')
	#price = models.FloatField(help_text='The price is the cost of the item.')
	
	class Meta:
		ordering = ['order', 'name']

	def __unicode__(self):
		return self.name



class Menu(models.Model):
	name = models.CharField(max_length=32, verbose_name='menu category name')
	additional_text = models.CharField(max_length=128, null=True, blank=True, help_text='The additional text is any bit of related information to go along with a menu category, i.e. the \'Pasta\' category might have details that say \'All entrees come with salad and bread\'.')
	order = models.IntegerField(default=0, help_text='The order is the order that this category should appear in when rendered on the templates.')
	
	class Meta:
		ordering = ['order', 'name']
	
	def __unicode__(self):
		return self.name