import json
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session

from ..auth import require_admin
from ..db import get_db
from ..models import BlogPost, Project, SiteSettings, Skill, Tag, Testimonial
from ..schemas import (
    BlogPostCreate,
    BlogPostOut,
    BlogPostUpdate,
    ProjectCreate,
    ProjectOut,
    ProjectUpdate,
    SiteSettingsOut,
    SiteSettingsUpdate,
    SkillCreate,
    SkillOut,
    TagCreate,
    TagOut,
    TestimonialCreate,
    TestimonialOut,
)
from ..utils import csv_to_list, list_to_csv, slugify

router = APIRouter(prefix="/admin", tags=["Admin"], dependencies=[Depends(require_admin)])


@router.post("/projects", response_model=ProjectOut)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    slug = payload.slug or slugify(payload.title)
    project = Project(
        title=payload.title,
        slug=slug,
        description=payload.description,
        content=payload.content,
        stack=list_to_csv(payload.stack),
        category=payload.category,
        cover_image=payload.cover_image,
        gallery_images=list_to_csv(payload.gallery_images),
        github_url=payload.github_url,
        live_url=payload.live_url,
        is_featured=payload.is_featured,
        updated_at=datetime.utcnow(),
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return ProjectOut(
        id=project.id,
        title=project.title,
        slug=project.slug,
        description=project.description,
        content=project.content,
        stack=csv_to_list(project.stack),
        category=project.category,
        cover_image=project.cover_image,
        gallery_images=csv_to_list(project.gallery_images),
        github_url=project.github_url,
        live_url=project.live_url,
        is_featured=project.is_featured,
        created_at=project.created_at,
        updated_at=project.updated_at,
    )


@router.put("/projects/{project_id}", response_model=ProjectOut)
def update_project(project_id: int, payload: ProjectUpdate, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.title = payload.title
    project.slug = payload.slug or slugify(payload.title)
    project.description = payload.description
    project.content = payload.content
    project.stack = list_to_csv(payload.stack)
    project.category = payload.category
    project.cover_image = payload.cover_image
    project.gallery_images = list_to_csv(payload.gallery_images)
    project.github_url = payload.github_url
    project.live_url = payload.live_url
    project.is_featured = payload.is_featured
    project.updated_at = datetime.utcnow()
    db.add(project)
    db.commit()
    db.refresh(project)
    return ProjectOut(
        id=project.id,
        title=project.title,
        slug=project.slug,
        description=project.description,
        content=project.content,
        stack=csv_to_list(project.stack),
        category=project.category,
        cover_image=project.cover_image,
        gallery_images=csv_to_list(project.gallery_images),
        github_url=project.github_url,
        live_url=project.live_url,
        is_featured=project.is_featured,
        created_at=project.created_at,
        updated_at=project.updated_at,
    )


@router.delete("/projects/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {"status": "deleted"}


@router.post("/blog", response_model=BlogPostOut)
def create_blog_post(payload: BlogPostCreate, db: Session = Depends(get_db)):
    slug = payload.slug or slugify(payload.title)
    published_at = datetime.utcnow() if payload.is_published else None
    post = BlogPost(
        title=payload.title,
        slug=slug,
        excerpt=payload.excerpt,
        content=payload.content,
        cover_image=payload.cover_image,
        tags=list_to_csv(payload.tags),
        is_published=payload.is_published,
        published_at=published_at,
        updated_at=datetime.utcnow(),
    )
    db.add(post)
    db.commit()
    db.refresh(post)
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


@router.put("/blog/{post_id}", response_model=BlogPostOut)
def update_blog_post(post_id: int, payload: BlogPostUpdate, db: Session = Depends(get_db)):
    post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    post.title = payload.title
    post.slug = payload.slug or slugify(payload.title)
    post.excerpt = payload.excerpt
    post.content = payload.content
    post.cover_image = payload.cover_image
    post.tags = list_to_csv(payload.tags)
    post.is_published = payload.is_published
    post.published_at = datetime.utcnow() if payload.is_published else None
    post.updated_at = datetime.utcnow()
    db.add(post)
    db.commit()
    db.refresh(post)
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


@router.delete("/blog/{post_id}")
def delete_blog_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    db.delete(post)
    db.commit()
    return {"status": "deleted"}


@router.post("/tags", response_model=TagOut)
def create_tag(payload: TagCreate, db: Session = Depends(get_db)):
    tag = Tag(name=payload.name, slug=payload.slug or slugify(payload.name))
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


@router.delete("/tags/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit()
    return {"status": "deleted"}


@router.post("/testimonials", response_model=TestimonialOut)
def create_testimonial(payload: TestimonialCreate, db: Session = Depends(get_db)):
    testimonial = Testimonial(
        full_name=payload.full_name,
        role=payload.role,
        company=payload.company,
        text=payload.text,
        avatar=payload.avatar,
    )
    db.add(testimonial)
    db.commit()
    db.refresh(testimonial)
    return testimonial


@router.delete("/testimonials/{testimonial_id}")
def delete_testimonial(testimonial_id: int, db: Session = Depends(get_db)):
    testimonial = db.query(Testimonial).filter(Testimonial.id == testimonial_id).first()
    if not testimonial:
        raise HTTPException(status_code=404, detail="Testimonial not found")
    db.delete(testimonial)
    db.commit()
    return {"status": "deleted"}


@router.post("/skills", response_model=SkillOut)
def create_skill(payload: SkillCreate, db: Session = Depends(get_db)):
    skill = Skill(name=payload.name, level=payload.level, category=payload.category)
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill


@router.delete("/skills/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    db.delete(skill)
    db.commit()
    return {"status": "deleted"}


@router.put("/settings", response_model=SiteSettingsOut)
def update_settings(payload: SiteSettingsUpdate, db: Session = Depends(get_db)):
    settings = db.query(SiteSettings).first()
    if not settings:
        settings = SiteSettings()
    settings.name = payload.name
    settings.title = payload.title
    settings.bio = payload.bio
    settings.socials = json.dumps(payload.socials)
    settings.meta_defaults = json.dumps(payload.meta_defaults)
    db.add(settings)
    db.commit()
    db.refresh(settings)
    return SiteSettingsOut(
        id=settings.id,
        name=settings.name,
        title=settings.title,
        bio=settings.bio,
        socials=payload.socials,
        meta_defaults=payload.meta_defaults,
    )


@router.post("/upload")
async def upload_file(file: UploadFile):
    content = await file.read()
    filename = file.filename or "upload.bin"
    path = f"backend/app/static/uploads/{filename}"
    with open(path, "wb") as handler:
        handler.write(content)
    return {"url": f"/static/uploads/{filename}"}
