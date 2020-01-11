from rest_framework import serializers
from .models import Menu,MenuCategory,MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'order','price']


class MenuCategorySerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuCategory
        fields = ['order', 'name', 'description','menuitem']



class MenuSerializer(serializers.ModelSerializer):
    menucategory = MenuCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ['name', 'additional_text', 'order','menucategory']
        
        
