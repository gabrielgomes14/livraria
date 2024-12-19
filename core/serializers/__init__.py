from .autor import AutorSerializer
from .categoria import CategoriaSerializer 
from .editora import EditoraSerializer
from .user import UserSerializer
from .livro import LivroDetailSerializer, LivroSerializer, LivroListSerializer
from .compra import (
    CompraListSerializer,
    CompraCreateUpdateSerializer,
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer,
    ItensCompraSerializer,
)