
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sa
from sqlalchemy.sql import text
import uuid

from customapp.models.models import db


class RawActivity(db.Model):
    __tablename__ = "master_group"
    id = db.Column(UUID(as_uuid=True), primary_key=True, index=True, default=lambda: uuid.uuid4().hex, unique=True)
    factory_id = db.Column(db.String(7))
    group_id = db.Column(db.String(20))
    group_name = db.Column(db.String(20))

    def __repr__(self):
        return f"{{master_group: {{  \
        id: {self.id}, \
        factory_id: {self.factory_id}, \
        group_id: {self.group_id} \
        group_name: {self.group_name} \
        }}}}"
