from flask import Flask

# Create the Flask app instance
def create_app():
    app = Flask(__name__)
    app.secret_key = 'bc8cf472cd5af2a92e0f1feea3fac5ce'  

    # Register routes (from routes.py)
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    return app
