from sqlalchemy.orm import Session

from . import models, schemas


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def get_category_posts(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def get_post_single(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def create_category(db: Session, item: schemas.CategoryCreate):
    db_item = models.Category(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_post(db: Session, item: schemas.PostCreate):
    db_item = models.Post(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
