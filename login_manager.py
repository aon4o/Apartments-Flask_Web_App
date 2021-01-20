from app_config import app
from flask_login import LoginManager, login_user, login_required, \
    logout_user, current_user
from database import User

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
