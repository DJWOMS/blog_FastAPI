from typing import List

from pydantic import BaseModel


class PostBase(BaseModel):
    """Base model schemas post"""
    title: str
    slug: str
    category_id: int

    class Config:
        orm_mode = True


class PostList(PostBase):
    pass


class PostCreate(PostBase):
    description: str


class PostSingle(PostBase):
    description: str


class CategoryBase(BaseModel):
    """Base model schemas category"""
    name: str
    slug: str

    class Config:
        orm_mode = True


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    is_active: bool


class CategoryGet(CategoryBase):
    id: int


class CategoryAndPosts(CategoryGet):
    post_list: List[PostList] = []



