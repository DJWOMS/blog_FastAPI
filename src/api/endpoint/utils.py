from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

from src.api.utils.security import get_current_active_superuser
from src.base.schemas import Msg
from src.user.schemas import User
from src.user.models import User as DBUser
from src.utils import send_test_email

router = APIRouter()


@router.post("/test-email/", response_model=Msg, status_code=201)
def test_email(
    email_to: EmailStr,
    current_user: DBUser = Depends(get_current_active_superuser)
):
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}
