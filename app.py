from app import app, db
from app.models import User, Calendar, Week, ToDoItem

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Calendar': Calendar, 'Week': Week, 'ToDoItem': ToDoItem}