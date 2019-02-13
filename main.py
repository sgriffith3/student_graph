from app.app import app
from app.views.views import blueprint
app.register_blueprint(blueprint)
app.run(debug=True)
