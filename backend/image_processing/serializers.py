from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
