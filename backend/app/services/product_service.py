
from sqlalchemy.orm import Session
from typing import List
from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository
from app.schemas.product import ProductResponse,ProductListResponse,ProductCreate
from fastapi import HTTPException,status


class ProductService:
    def __init__(self,db:Session):
        self.product_repository=ProductRepository(db)
        self.category_repository=CategoryRepository(db)

    def get_all_products(self) ->ProductListResponse:
        products=self.product_repository.get_all()
        products_response=[ProductListResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=products_response,total=len(products_response))

    def get_product_by_id(self,product_id:int)->ProductResponse:
        product=self.product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Продукт с {product_id} не найден")

        return ProductResponse.model_validate(product)


    def get_products_by_cayegory(self,category_id:int)->ProductListResponse:
        category=self.product_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Категория товара с {category_id} не найдена")

        products=self.product_repository.get_by_category(category_id)
        products_response=[ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=products_response,total=len(products_response))

    def create_products(self,product_data:ProductCreate)->ProductResponse:
        category=self.category_repository.get_by_id(product_data.categogory_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Категории товара с {product_date} не найдена")
        product=self.product_repository.create(product_data)
        return ProductResponse.model_validate(product)