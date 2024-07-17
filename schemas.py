from pydantic import BaseModel
from typing import List, Optional, Dict


class TranslatedString(BaseModel):
    language: str
    text: str


class QuotaDefinition(BaseModel):
    type: Optional[str]
    description: Dict[str, str]
    reset_interval: Optional[str]
    scope: str
    feature: Optional[str] = None


class QuotaGet(BaseModel):
    limit: int
    used: int
    type: Optional[str]
    scope: str
    feature: Optional[str] = None
    user_id: Optional[str] = None


class QuotaUpdate(BaseModel):
    limit: int
    scope: str
    feature: Optional[str] = None
    user_id: Optional[str] = None


class Metadata(BaseModel):
    tool_url: str
    quota_url: str
    image_url: str
    description: Dict[str, str]
    title: Dict[str, str]
    supported_quotas: List[QuotaDefinition]
