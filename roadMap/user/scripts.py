from user.utils import add_permission_to_model
from user.models import Mentor


add_permission_to_model(Mentor,"view_courses","Mentor can view own courses")
