from flask import Flask, Blueprint, jsonify, request
from app.api.v1.models.user_model import User

users = Blueprint('users', __name__)

@users.route('/')
def hello():
    return "Testing the app from users"