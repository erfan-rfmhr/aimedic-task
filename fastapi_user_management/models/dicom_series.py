"""dicom_series table."""
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from fastapi_user_management.models.base import Base
from fastapi_user_management.models.user_role import UserRoleModel  # noqa: F401


class DicomSeriesModel(Base):
    """DicomSeriesModel known as dicom_series table."""

    __tablename__ = "dicom_series"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    StudyInstanceUID: Mapped[str] = mapped_column(String)
    SeriesInstanceUID: Mapped[str] = mapped_column(String)
    Modality: Mapped[str] = mapped_column(String)
    BodyPartExamined: Mapped[str] = mapped_column(String)
    PatientID: Mapped[int] = mapped_column(Integer, ForeignKey("user_account.id"))
