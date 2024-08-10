# Third-Party Dependencies
from sqlmodel import Field, Relationship

# Local Dependencies
from src.core.common.models import SoftDeleteMixin, TimestampMixin, UUIDMixin, Base
from src.apps.ms.genres.models import Genre
from src.apps.ms.subgenres.models import Subgenre


class LabelProfileBase(Base):
    label_name: str = Field(
        max_length=255,
        nullable=False,
        description="Label Name",
        schema_extra={"examples": ["Electronic"]},
    )
    email: str = Field(
        max_length=255,
        nullable=False,
        description="Label Email",
        schema_extra={"examples": ["info@label.com"]},
    )
    biography: str = Field(
        max_length=1000,
        nullable=True,
        description="Label Biography",
        schema_extra={"examples": ["This is the biography of the label."]},
    )
    established_year: int = Field(
        nullable=True,
        description="Year the label was established",
        schema_extra={"examples": [1990]},
    )


class Labels(
    UUIDMixin,
    LabelProfileBase,
    TimestampMixin,
    SoftDeleteMixin,
    table=True,
):
    __tablename__ = "ms_label"
    __table_args__ = ({"comment": "Management System label information"},)

    genres: list["Genre"] = Relationship(
        back_populates="label",
        sa_relationship_kwargs={"primaryjoin": "Labels.id == Genre.label_id"},
    )
    subgenres: list["Subgenre"] = Relationship(
        back_populates="label",
        sa_relationship_kwargs={"primaryjoin": "Labels.id == Subgenre.label_id"},
    )
