from django.db import models
from base.models import BaseModel


class JobStatus(models.TextChoices):
    OPEN = "open"
    CLOSED = "closed"


class JobLocationType(models.TextChoices):
    REMOTE = "remote"
    ONSITE = "onsite"
    HYBRID = "hybrid"


class JobApplicationStatus(models.TextChoices):
    PENDING = "pending"
    REJECTED = "rejected"
    ACCEPTED = "accepted"


class JobTag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Create your models here.
class Job(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10, choices=JobStatus.choices, default=JobStatus.OPEN
    )
    location_type = models.CharField(
        max_length=10, choices=JobLocationType.choices, default=JobLocationType.REMOTE
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    tags = models.ManyToManyField(JobTag)

    def __str__(self):
        return self.title


class JobApplication(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=JobApplicationStatus.choices,
        default=JobApplicationStatus.PENDING,
    )
    candidate = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"{self.job.title} - {self.created_at} - {self.status}"
