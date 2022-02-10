from courses.utils import add_custom_permission_to_model

from courses.models import CourseChapterMedia

### add permission for publish video
add_custom_permission_to_model(CourseChapterMedia, "can_publish", "mentor can publish video for course")