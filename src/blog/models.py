from sqlalchemy import String, Integer, ForeignKey, Boolean, Column
from sqlalchemy.orm import relationship
from db.base_class import Base
from src.user.models import User


class Category(Base):
    """Model category"""
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    slug = Column(String, unique=True)
    is_active = Column(Boolean(), default=True)

    post = relationship("Post", back_populates="category")


class Post(Base):
    """Model post"""
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    slug = Column(String, unique=True)

    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="post")

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User, back_populates="post")
