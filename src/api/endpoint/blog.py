from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.utils.db import get_db
from src.blog import service, schemas

router = APIRouter()


@router.post("/category/", response_model=schemas.CategoryCreate)
async def create_category(item: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return service.create_category(db=db, item=item)


@router.get("/category/", response_model=List[schemas.CategoryGet])
async def get_category_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_categories(db=db, skip=skip, limit=limit)


@router.get("/category/{category_id}", response_model=schemas.CategoryAndPosts)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return service.get_category_posts(db=db, category_id=category_id)


@router.post("/post/", response_model=schemas.PostCreate)
def create_post(item: schemas.PostCreate, db: Session = Depends(get_db)):
    return service.create_post(db=db, item=item)


@router.get("/post/", response_model=List[schemas.PostList])
def get_post_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_posts(db=db, skip=skip, limit=limit)


@router.get("/post/{post_id}", response_model=schemas.PostSingle)
def get_post_detail(post_id: int, db: Session = Depends(get_db)):
    return service.get_post_single(db=db, post_id=post_id)
