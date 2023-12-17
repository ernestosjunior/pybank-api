from app import create_app

app = create_app()

app.run(debug=True, port=3333, host="0.0.0.0")
