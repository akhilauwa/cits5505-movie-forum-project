from app import create_app, db
from app.models import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    #TODO: Add the models to the shell context
    return {'db': db,
            'User': User}
    