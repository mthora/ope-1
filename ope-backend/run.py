from src.main.config import app, api

if __name__ == "__main__":
    api.init_app(app)
    app.run(host='0.0.0.0')
