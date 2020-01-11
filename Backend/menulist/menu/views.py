from rest_framework import generics
from .models import Menu,MenuCategory,MenuItem
from .serializers import MenuCategorySerializer,MenuSerializer,MenuItemSerializer
class ListMenuCategory(generics.ListAPIView):
    queryset = MenuCategory.objects.order_by('order')
    serializer_class = MenuCategorySerializer
class ListMenu(generics.ListAPIView):
    queryset = Menu.objects.order_by('order')
    serializer_class = MenuSerializer
class ListMenuItem(generics.ListAPIView):
    queryset = MenuItem.objects.order_by('order')
    serializer_class = MenuItemSerializer
     