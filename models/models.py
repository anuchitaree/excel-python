from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sa
from sqlalchemy.sql import text
import uuid

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    Migrate(app, db)

# import your model file in app.py

# from customapp.models.master_setting.master_group_line_mc import *
# from customapp.models.system_admin.grpc_interface import *
