"""CRUD for DicomSeriesModel."""
from sqlalchemy.orm import Session

from fastapi_user_management.crud.crud_base import CreateSchemaType, CRUDBase, ModelType
from fastapi_user_management.models.dicom_series import DicomSeriesModel
from fastapi_user_management.schemas.dicom import DicomSeries


class CRUDDicom(CRUDBase[DicomSeriesModel, DicomSeries, DicomSeries]):
    """CRUD for dicom_series database model."""

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """Create new user.

        Args:
            db (Session): database session
            obj_in (DicomSeries): dicom data based on schema

        Returns:
            DicomSeriesModel: created dicom
        """
        db_obj = self.model(
            StudyInstanceUID=obj_in.study_instance_uid,
            SeriesInstanceUID=obj_in.series_instance_uid,
            Modality=obj_in.modality,
            BodyPartExamined=obj_in.body_part_examined,
            PatientID=obj_in.patient_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


dicom = CRUDDicom(DicomSeriesModel)
