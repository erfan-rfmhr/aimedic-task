"""Dicom schemas."""

from fastapi import Header
from pydantic import BaseModel


class DicomSeries(BaseModel):
    """Dicom series schema."""

    study_instance_uid: str = Header(...)
    series_instance_uid: str = Header(...)
    modality: str = Header(...)
    body_part_examined: str = Header(...)
    patient_id: int
