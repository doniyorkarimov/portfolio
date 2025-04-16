from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from tinymce.models import HTMLField


class CustomUser(AbstractUser):
    pass



class AboutMe(models.Model):
    """About me model"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    about_me = HTMLField(null=True, blank=True, help_text="Write something about yourself")
    image = models.ImageField(upload_to='about_me/image', blank=True, null=True)
    skills = models.ManyToManyField("Skill", blank=True, help_text="Add your skills")
    my_name = models.CharField(max_length=100, help_text="Enter your name")
    social_media = models.JSONField(null=True, blank=True, help_text="Add your social media links")

    def __str__(self):
        return  self.my_name



class Education(models.Model):
    """Education model"""
    about_me = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    start_year = models.CharField(max_length=4, help_text="Start year, e.g., 2005")
    end_year = models.CharField(max_length=4, help_text="End year, e.g., 2008")
    degree = models.CharField(max_length=100, help_text="Degree, e.g., Bachelor of Science")
    university = models.CharField(max_length=100, help_text="University, e.g., University of Miami")
    description = HTMLField(help_text="Description, e.g., Bachelor of Science in Computer Science")

    def __str__(self):
        return f"{self.degree} at {self.university} ({self.start_year}-{self.end_year})"


class Experience(models.Model):
    """Experience model"""
    about_me = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    start_year = models.CharField(max_length=4, help_text="Start year, e.g., 2005")
    end_year = models.CharField(max_length=4, help_text="End year, e.g., 2008")
    position = models.CharField(max_length=100, help_text="Position, e.g., Software Engineer")
    company = models.CharField(max_length=100, help_text="Company, e.g., Google")
    description = HTMLField(help_text="Description, e.g., Software Engineer at Google")

    def __str__(self):
        return f"{self.position} at {self.company} ({self.start_year}-{self.end_year})"


class Skill(models.Model):
    """Skill model"""
    name = models.CharField(max_length=100, unique=True, help_text="Enter your skill name")

    def __str__(self):
        return self.name



class Project(models.Model):
    """Project model"""
    title = models.CharField(max_length=100, help_text="Enter your project title")
    year = models.CharField(max_length=4, help_text="Year, e.g., 2018")
    client = models.CharField(max_length=100, null=True, blank=True, help_text="Client, e.g., Google")
    service = models.CharField(max_length=100, null=True, blank=True, help_text="Service, e.g., Web Development")
    project_type = models.CharField(max_length=50, help_text="Project type e.g., Full Stack")
    description = HTMLField(null=True, blank=True, help_text="Details about the project")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    is_active = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.year})"



class ProjectImage(models.Model):
    """Project image model"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project/image', help_text="Upload your project image")

    def __str__(self):
        return f"Image for {self.project.title}"


class YoutubeVideo(models.Model):
    """Youtube video model"""
    title = models.CharField(max_length=100, help_text="Enter your video title")
    link = models.URLField(help_text="Enter your video link")
    thumbnail = models.ImageField(upload_to="image/youtube_thumbnail", help_text="Youtube video thumbnail")
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name