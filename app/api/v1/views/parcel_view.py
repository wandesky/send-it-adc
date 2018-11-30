from flask import Flask, Blueprint, jsonify, request
from app.api.v1.models.parcel_model import Parcel

parcels = Blueprint('parcels', __name__)

@parcels.route('/')
def hello():
    return "Testing the app from parcels"