from fastapi import APIRouter

from app.models.researcher import UserProfile
from app.resources.researcher_resource import UserResource
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/user_profile/{user_id}", tags=["users"])
async def get_researcher(user_id: str) -> UserProfile:

    # TODO Do lifecycle management for singleton resource
    res = ServiceFactory.get_service("UserResource")
    result = res.get_by_key(user_id)
    return result

