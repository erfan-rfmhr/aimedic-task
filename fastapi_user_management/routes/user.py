"""User endpoint: /user."""
from typing import Annotated

from fastapi import APIRouter, Depends, File, Header, UploadFile, status
from sqlalchemy.orm import Session

from fastapi_user_management import crud
from fastapi_user_management.core.database import get_db
from fastapi_user_management.models.user import UserModel
from fastapi_user_management.routes import auth
from fastapi_user_management.schemas.dicom import DicomSeries
from fastapi_user_management.schemas.user import UserProfile

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal Server Error"},
    },
)


@router.get("/profile", response_model=UserProfile)
async def get_user_profile(
    user: Annotated[UserModel, Depends(auth.get_current_active_user)]
):
    """Get user profile."""
    return user


@router.post("/upload-dicom/")
async def upload_dicom(
    current_user: Annotated[UserModel, Depends(auth.get_current_active_user)],
    file: UploadFile = File(...),
    study_instance_uid: str = Header(...),
    series_instance_uid: str = Header(...),
    modality: str = Header(...),
    body_part_examined: str = Header(...),
    db: Session = Depends(get_db),
):
    """Get uploaded file."""
    obj = DicomSeries(
        study_instance_uid=study_instance_uid,
        series_instance_uid=series_instance_uid,
        modality=modality,
        body_part_examined=body_part_examined,
        patient_id=current_user.id,
    )
    crud.dicom.create(db=db, obj_in=obj)

    return {"filename": file.filename}
