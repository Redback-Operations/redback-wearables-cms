from flask import Blueprint

# Import blueprints from other route files
from .auth import bp as auth_bp


# If we have more route files, import their blueprints here

# Create a main blueprint to combine all others
main_bp = Blueprint('main', __name__)

# Register other blueprints with the main blueprint
main_bp.register_blueprint(auth_bp, url_prefix='/auth')

# If we have more blueprints, register them here

# This function will be called in the app factory to register all routes
def init_app(app):
    app.register_blueprint(main_bp)