from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import BlogPost
from ..schemas import BlogPostOut
from ..utils import csv_to_list

router = APIRouter(prefix="/blog", tags=["Blog"])


def serialize_post(post: BlogPost) -> BlogPostOut:
    return BlogPostOut(
        id=post.id,
        title=post.title,
        slug=post.slug,
        excerpt=post.excerpt,
        content=post.content,
        cover_image=post.cover_image,
        tags=csv_to_list(post.tags),
        is_published=post.is_published,
        views=post.views,
        likes=post.likes,
        created_at=post.created_at,
        updated_at=post.updated_at,
        published_at=post.published_at,
    )


@router.get("", response_model=list[BlogPostOut])
def list_posts(
    search: str | None = None,
    tag: str | None = None,
    skip: int = 0,
    limit: int = Query(default=20, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(BlogPost).filter(BlogPost.is_published.is_(True))
    if search:
        query = query.filter(BlogPost.title.ilike(f"%{search}%"))
    if tag:
        query = query.filter(BlogPost.tags.ilike(f"%{tag}%"))
    posts = query.order_by(BlogPost.published_at.desc()).offset(skip).limit(limit).all()
    return [serialize_post(post) for post in posts]


@router.get("/{slug}", response_model=BlogPostOut)
def get_post(slug: str, db: Session = Depends(get_db)):
    post = db.query(BlogPost).filter(BlogPost.slug == slug, BlogPost.is_published.is_(True)).first()
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    post.views += 1
    db.add(post)
    db.commit()
    db.refresh(post)
    return serialize_post(post)
