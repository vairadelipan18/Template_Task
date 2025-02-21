import os
from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
from flask_cors import CORS
import dns.resolver


dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ["8.8.8.8", "8.8.4.4"]

load_dotenv()

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["MONGODB_SETTINGS"] = {
        "host": os.getenv("MONGO_URI"), 
        "connect": False  
    }

    db.init_app(app)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from app.urls import register_routes
    register_routes(app)

    return app
