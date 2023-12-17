from app import create_app
from app.routes import register_routes

app = create_app()

register_routes(app)

app.run(debug=True, port=3333, host="0.0.0.0")
