from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=6)


class UserOut(UserBase):
    id: int
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True


class ProjectBase(BaseModel):
    title: str
    description: str
    content: str
    stack: List[str] = []
    category: str = ""
    cover_image: str = ""
    gallery_images: List[str] = []
    github_url: str = ""
    live_url: str = ""
    is_featured: bool = False


class ProjectCreate(ProjectBase):
    slug: Optional[str] = None


class ProjectUpdate(ProjectBase):
    slug: Optional[str] = None


class ProjectOut(ProjectBase):
    id: int
    slug: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class BlogPostBase(BaseModel):
    title: str
    excerpt: str = ""
    content: str
    cover_image: str = ""
    tags: List[str] = []
    is_published: bool = False


class BlogPostCreate(BlogPostBase):
    slug: Optional[str] = None


class BlogPostUpdate(BlogPostBase):
    slug: Optional[str] = None


class BlogPostOut(BlogPostBase):
    id: int
    slug: str
    views: int
    likes: int
    created_at: datetime
    updated_at: datetime
    published_at: Optional[datetime]

    class Config:
        from_attributes = True


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    slug: Optional[str] = None


class TagOut(TagBase):
    id: int
    slug: str

    class Config:
        from_attributes = True


class TestimonialBase(BaseModel):
    full_name: str
    role: str = ""
    company: str = ""
    text: str
    avatar: str = ""


class TestimonialCreate(TestimonialBase):
    pass


class TestimonialOut(TestimonialBase):
    id: int

    class Config:
        from_attributes = True


class SkillBase(BaseModel):
    name: str
    level: int = Field(ge=0, le=100)
    category: str = ""


class SkillCreate(SkillBase):
    pass


class SkillOut(SkillBase):
    id: int

    class Config:
        from_attributes = True


class SiteSettingsBase(BaseModel):
    name: str = ""
    title: str = ""
    bio: str = ""
    socials: dict = {}
    meta_defaults: dict = {}


class SiteSettingsUpdate(SiteSettingsBase):
    pass


class SiteSettingsOut(SiteSettingsBase):
    id: int

    class Config:
        from_attributes = True


class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    message: str


class ContactOut(ContactCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
