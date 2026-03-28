from flask import Blueprint

taking_bp = Blueprint('taking', __name__)

from . import routes
