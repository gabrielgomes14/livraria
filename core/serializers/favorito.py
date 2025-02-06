from rest_framework.serializers import (
    DecimalField,
    IntegerField,
    ModelSerializer,
    Serializer,
    SlugRelatedField,
    ValidationError,
)
from core.models import Favorito
from uploader.models import Image
from uploader.serializers import ImageSerializer


class FavoritoAlterarPrecoSerializer(ModelSerializer):
    preco = DecimalField(max_digits=10, decimal_places=2)

    def validate_preco(self, value):
        """Valida se o preço é um valor positivo."""
        if value <= 0:
            raise ValidationError("O preço deve ser um valor positivo.")
        return value


class FavoritoAjustarEstoqueSerializer(Serializer):
    avaliacao = IntegerField()

    def validate_avaliacao(self, value):
        favorito = self.context.get("favorito")
        if favorito:
            nova_avaliacao = favorito.avaliacao + value
            if nova_avaliacao < 0:
                raise ValidationError("A avaliação em favoritos não pode ser negativa.")
            if nova_avaliacao > 10:
                raise ValidationError("A avaliação não pode ser maior que 10.")
        return value


class FavoritoSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa", queryset=Image.objects.all(), slug_field="attachment_key", required=False, write_only=True
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Favorito
        fields = "__all__"
        depth = 1


class FavoritoListSerializer(ModelSerializer):
    class Meta:
        model = Favorito
        fields = ("id", "titulo", "preco")


class FavoritoRetrieveSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Favorito
        fields = "__all__"
        depth = 1
