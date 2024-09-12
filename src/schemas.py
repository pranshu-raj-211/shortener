from pydantic import BaseModel, HttpUrl

class URLBase(BaseModel):
    target_url: HttpUrl

class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True

class URLInfo(URL):
    url: str
    admin_url: str