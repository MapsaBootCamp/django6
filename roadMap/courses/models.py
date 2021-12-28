from django.db import models
from django.utils.translation import gettext as _

from user.models import Mentor, Profile
from .validators import JSONSchemaValidator

class CourseCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.title


class Course(models.Model):
    MY_JSON_FIELD_SCHEMA = {
    'schema': 'Course history schema',
    'type': 'object',
    'properties': {
        'students': {
            'type': 'array',
        }
    },
    'required': ['students']
    }

    name = models.CharField(verbose_name=_("name"), help_text="نام دوره", max_length=255)
    mentor = models.ManyToManyField(Mentor, related_name="mentors")
    category = models.ForeignKey(CourseCategory, related_name = "courses", on_delete= models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    img = models.ImageField(upload_to="course/images/", null=True, blank=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    students = models.ManyToManyField(Profile, related_name="students", through="CourseStudent")
    class_history = models.JSONField(
        default=dict,
        validators=[JSONSchemaValidator(limit_value=MY_JSON_FIELD_SCHEMA)]
        )

    def __str__(self) -> str:
        return self.name

class CourseChapter(models.Model):
    title = models.CharField(max_length=255)
    season_chapter = models.SmallIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self) -> str:
        return f"{self.season_chapter} - {self.title}"


class CourseChapterMedia(models.Model):

    COURSE_CONTETN_CHOICES = [
        ('video', 'Video'),
        ('picture', 'Picture'),
        ('voice', 'Voice'),
        ('pdf', 'PDF')
    ]

    content = models.FileField(upload_to="course/contents/")
    type_content = models.CharField(max_length=10, choices=COURSE_CONTETN_CHOICES)
    update_field = models.DateTimeField(auto_now=True)
    course_chapter = models.ForeignKey(CourseChapter, on_delete=models.CASCADE)


class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return super().__str__()