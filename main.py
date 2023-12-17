from app import create_app
from app.blueprints import register_blueprints

app = create_app()

register_blueprints(app)

app.run(debug=True, port=3333, host="0.0.0.0")
