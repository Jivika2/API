
from rest_framework import serializers
from .models import Category, Book, Product

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
         fields="__all__"
         model = Category 
'''   fields = (
            'id',
            'title'
        )'''
         


class BookSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)
    class Meta:
        fields="__all__"
        model = Book
''' fields = (
            'id',
            'title',
            'category',
            'author',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'created_by',
            'status',
            'date_created'
        )'''
       

class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)
    class Meta:
         fields="__all__"
         model = Product
'''        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'imageUrl',
            'created_by',
            'status',
            'date_created'
        )'''
        
