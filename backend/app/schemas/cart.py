
from pydantic import BaseModel,Field
from typing import Optional


class CartItemBase(BaseModel):
    product_id: int = Field(...,description="Product ID")
    quantity: int = Field(...,gt=0,description="Количество не может быть меньше 0")



class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
     product_id: int = Field(...,description="Product ID")
     quantity: int = Field(...,gt=0,description="Количество добавленых продуктов не может быть меньше 0")


class CartItem(BaseModel):
    product_id: int
    name: str=Field(...,description="Название продукта")
    price: float=Field(...,description="Стоимость товара")
    quantity: int= Field(..., description="Кол-во товара")
    subtotal: float= Field(...,description="стоимость заказа(price*quantity)")
    imege_url:Optional[str]=Field(None,description="Продукт злемент Url")

class CartResponse(BaseModel):
    items:list[CartItem]=Field(...,description="лист элементов корзины")
    total: float=Field(...,description="стоимость корзины")
    items_count: int =Field(..., description="обшее количества товаров")