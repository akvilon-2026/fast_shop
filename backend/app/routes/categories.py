
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.services.category_service import CategoryService
from app.schemas.category import CategoryResponse

router = APIRouter(prefix="/app/categories", tags=["Категории товаров"])

@router.get("", response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):        
    service = CategoryService(db)  # Создаем экземпляр сервиса
    return service.get_all_categories()  # Вызываем метод


@router.get("/{category_id}",response_model=CategoryService,status_code=status.HTTP_200_OK)
def get_cateqory(category_id:int,db: Session=Depends(get_db)):
    service=CategoryService(db)
    return service.get_category_by_id(category_id)



