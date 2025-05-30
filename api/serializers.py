from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'stock',
        )

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must bes greater than 0"
            )
        return value