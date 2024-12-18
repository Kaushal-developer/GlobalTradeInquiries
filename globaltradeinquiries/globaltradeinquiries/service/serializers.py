from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model.
    """

    class Meta:
        model = Category
        fields = ['id', 'name','image', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']  # Read-only fields

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.
    """
    # Include category details using the related CategorySerializer
    category = CategorySerializer(read_only=True)  # For nested read-only data
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',  # Maps to the 'category' field in the model
        write_only=True
    )

    # URL for the product image (if needed)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock',
            'category', 'category_id', 'image', 'image_url',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']  # Fields that can't be updated

    def get_image_url(self, obj):
        """
        Return the full URL of the product image.
        """
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
