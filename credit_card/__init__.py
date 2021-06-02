import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
from dotenv import load_dotenv
load_dotenv()

# load_dotenv()

# DATABASE_URI = os.getenv('DATABASE_URL')
# APP_SECRETKEY = os.getenv('APP_SECRETKEY')


db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)
    
    if app.config["ENV"] == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from credit_card.routes import (main_route, user_route)
    app.register_blueprint(main_route.bp)
    app.register_blueprint(user_route.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
