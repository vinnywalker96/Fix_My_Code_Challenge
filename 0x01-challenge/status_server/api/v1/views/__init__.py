#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from v1.views.index import *
