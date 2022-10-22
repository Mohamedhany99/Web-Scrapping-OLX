from rest_framework import serializers

from OLX.models import Items

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['is_on_sale'] = instance.is_on_sale()
        # data['current_price'] = instance.current_price()
        return data
