from pydantic import BaseModel,Field

class CategoryBase(BaseModel):
    name: str=Field(...,min_length=5,max_length=100,description="Category name")
    slug: str=Field(...,min_length=5,max_length=100,description="URL_friend category name") # ..., обязательные поля



class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int = Field(...,description="category identifler")
    
    class Config:
        form_attributes=True