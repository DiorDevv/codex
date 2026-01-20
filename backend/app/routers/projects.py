from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Project
from ..schemas import ProjectOut
from ..utils import csv_to_list

router = APIRouter(prefix="/projects", tags=["Projects"])


def serialize_project(project: Project) -> ProjectOut:
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


@router.get("", response_model=list[ProjectOut])
def list_projects(
    search: str | None = None,
    category: str | None = None,
    stack: str | None = None,
    is_featured: bool | None = None,
    skip: int = 0,
    limit: int = Query(default=20, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(Project)
    if search:
        query = query.filter(Project.title.ilike(f"%{search}%"))
    if category:
        query = query.filter(Project.category == category)
    if stack:
        query = query.filter(Project.stack.ilike(f"%{stack}%"))
    if is_featured is not None:
        query = query.filter(Project.is_featured == is_featured)
    projects = query.offset(skip).limit(limit).all()
    return [serialize_project(project) for project in projects]


@router.get("/{slug}", response_model=ProjectOut)
def get_project(slug: str, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.slug == slug).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return serialize_project(project)
