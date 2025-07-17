from rest_framework import serializers


class LexcomFiveClassSerializer(serializers.Serializer):
    very_good = serializers.FloatField()
    good = serializers.FloatField()
    normal = serializers.FloatField()
    bad = serializers.FloatField()
    very_bad = serializers.FloatField()

    class Meta:
        # Establecer un nombre específico para la representación JSON
        # Puedes usar `field` para personalizar los nombres de los campos
        # en tu representación JSON
        fields = ('very_good', 'good', 'normal', 'bad', 'very_bad')


class LexcomBinaryClassSerializer(serializers.Serializer):
    success = serializers.FloatField()
    failure = serializers.FloatField()

    class Meta:
        fields = ('success', 'failure')
