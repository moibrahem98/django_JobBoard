from django.db import models
from django.contrib.auth.models import User
# Create your models here.


JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)


class Job(models.Model):
    # owner = models.ForeignKey(
    #     User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=300)
    puplished_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # image = models.ImageField(upload_to=image_upload)
    # slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title
