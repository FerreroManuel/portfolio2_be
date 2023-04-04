from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _



PROJECT_STATUS_CHOICES = [
    ("DEV", _("En desarrollo")),
    ("PRO", _("En producción")),
    ("PAU", _("Pausado")),
    ("CAN", _("Cancelado")),
]


class Developer(models.Model):
    """
    Class that manage personal information to show on website

    personal information.
    firstname: Firstname/s
    lastname: Lastname/s
    phone: Cellphone with whatsapp
    email: Email
    residence: City, State - Country
    photo: Photo without background (to make possible dark/light themes)
           (it will be uploaded on the external server provided)
    about: Cover letter
    aboutShort: Very short cover letter
    cvEsp: Resume PDF in spanish (it will be uploaded on the external server provided)
    cvEng: Resume PDF in english (it will be uploaded on the external server provided)
    """
    firstName = models.CharField(_('Nombre/s'), max_length=30)
    lastName = models.CharField(_('Apellido/s'), max_length=30)
    openToWork = models.BooleanField(_('¿Buscando trabajo?'), default=True)
    jobTitle = models.CharField(_('Título de trabajo'), max_length=60)
    phone = models.CharField(_('Teléfono'), max_length=13)
    email = models.EmailField(_('Email'))
    residence = models.CharField(_('Residencia'), max_length=120, help_text=_("Ej.: Ciudad, Provincia - País"))
    photo = models.ImageField(_('Foto'), upload_to="img/about/", help_text=_("Preferentemente imagen con fondo transparente"))
    about = models.TextField(_('Carta de presentación'))
    aboutShort = models.TextField(_('Presentación corta'))
    cvEsp = models.FileField(_('CV en español'), upload_to="files/cv/")
    cvEng = models.FileField(_('CV en inglés'), upload_to="files/cv/")

    class Meta:
        verbose_name = _('Información personal')
        verbose_name_plural = _('Información personal')

    def __str__(self) -> str:
        return f"{self.lastName}, {self.firstName}"


class Title(models.Model):
    """
    Keywords which will be shown at home with typing effect before Jr. Developer.
    Eg.: Python jr. devloper. Where Python is the keyword storaged at Title model

    developer: Foreign key to Developer object
    title: keyword
    """
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="title", verbose_name=_("Desarrollador"))
    title = models.CharField(_("Título"), max_length=30)

    class Meta:
        verbose_name = _('Título')
        verbose_name_plural = _('Títulos')

    def __str__(self) -> str:
        return self.title


class SocialLink(models.Model):
    """
    Links to social profiles, like linkedin, github, etc
    
    developer: Foreign key to Developer object
    title: Name of the social network
    icon: HTML class of icon to show on website
    link: URL to profile
    isActive: Enable/disable the item
    """
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="social_link", verbose_name=_("Desarrollador"))
    title = models.CharField(_('Nombre'), max_length=30)
    icon = models.CharField(_('Ícono'), max_length=120)
    link = models.URLField(_('Link'))
    isActive = models.BooleanField(_('¿Activo?'), default=True)

    class Meta:
        verbose_name = _('Social link')
        verbose_name_plural = _('Social links')

    def __str__(self) -> str:
        return self.title


class Language(models.Model):
    """
    Languages that the developer speak and his/her proficiency on each one

    developer: Foreign key to Developer object
    title: Name of language in spanish
    proficiency: Proficiency speaking the language (Between 1 and 100)
    isActive: Enable/disable the item
    """
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="language", verbose_name=_("Desarrollador"))
    title = models.CharField(_("Idioma"), max_length=30)
    proficiency = models.PositiveIntegerField(_("Competencia"), validators=[MinValueValidator(1), MaxValueValidator(100)], help_text=_("Entre 1 y 100"))
    isActive = models.BooleanField(_("¿Activo?"), default=True)

    class Meta:
        verbose_name = _('Idioma')
        verbose_name_plural = _('Idiomas')

    def __str__(self) -> str:
        return self.title


class Skill(models.Model):
    """
    Programming languages that the developer speak and his/her proficiency on each one

    developer: Foreign key to Developer object
    title: Name of language
    proficiency: Proficiency speaking the language (Between 0 and 100)
    isActive: Enable/disable the item
    """
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="skill", verbose_name=_("Desarrollador"))
    title = models.CharField(_("Habilidad"), max_length=30)
    proficiency = models.PositiveIntegerField(_("Competencia"), validators=[MinValueValidator(1), MaxValueValidator(100)], help_text=_("Entre 1 y 100"))
    isActive = models.BooleanField(_("¿Activo?"), default=True)

    class Meta:
        verbose_name = _('Habilidad')
        verbose_name_plural = _('Habilidades')

    def __str__(self) -> str:
        return self.title


class Framework(models.Model):
    """
    Framework or library of a programming language that developer knows

    skill: Foreign key to Skill object
    title: Name of framework or library
    icon: HTML icon to show on website
    isActive: Enable/disable the item
    """
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="framework", verbose_name=_("Habilidad"))
    title = models.CharField(_("Framework/Librería"), max_length=30)
    icon = models.CharField(_("Ícono HTML"), max_length=120)
    isActive = models.BooleanField(_("¿Activo?"), default=True)

    class Meta:
        verbose_name = _('Framework')
        verbose_name_plural = _('Frameworks')

    def __str__(self) -> str:
        return f"{self.title} ({self.skill})"


class Repository(models.Model):
    """
    Public repository of a project on Github, Gitlab or similar

    title: Name of repository
    link: URL to the repository
    readmeEspLink: URL to the README file's spanish section
    readmeEngLink: URL to the README file's english section
    """
    title = models.CharField(_("Nombre"), max_length=30)
    link = models.URLField(_("Link"))
    readmeLink = models.URLField(_("Link a README.md"))

    class Meta:
        verbose_name = _('Repositorio')
        verbose_name_plural = _('Repositorios')

    def __str__(self) -> str:
        return self.title


class Education(models.Model):
    """
    Course or career studied or studying by the developer

    developer: Foreign key to Developer object
    title: Name of course/career
    place: Institution which offers the course/career
    link: URL to course/career (optional)
    startDate: Course/career start date
    finishDate: Course/career finish date (optional)
    isPresent: Determines if is currently being studied (optional)
    description: Description about course/career
    certificate: Certificate file (optional)
    repository: Repository which contains the project sourcecode (optional)
    isActive: Enable/disable the item
    """
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="education", verbose_name=_("Desarrollador"))
    title = models.CharField(_("Título"), max_length=120)
    place = models.CharField(_("Institución"), max_length=120)
    link = models.CharField(_("Link"), max_length=120, null=True, blank=True, help_text=_("Opcional"))
    startDate = models.DateField(_("Fecha inicio"))
    finishDate = models.DateField(_("Fecha final"), null=True, blank=True, help_text=_("Opcional"))
    isPresent = models.BooleanField(_("Cursando actualmente"), default=False)
    description = models.TextField(_("Descripción"))
    certificate = models.FileField(_("Certificado"), upload_to="files/certificates/", null=True, blank=True, help_text=_("Opcional"))
    repository = models.ForeignKey(Repository, on_delete=models.SET_NULL, related_name="edu_repo",blank=True, null=True, verbose_name=_("Repositorio"))
    isActive = models.BooleanField(_("¿Activo?"), default=True)

    class Meta:
        verbose_name = _('Educación')
        verbose_name_plural = _('Educación')

    def __str__(self) -> str:
        return self.title


class ProjectCategory(models.Model):
    """
    Category to which projects can be part

    titlEsp: Name of category
    """
    title = models.CharField(_("Categoría"), max_length=30)

    class Meta:
        verbose_name = _('Categoría de proyectos')
        verbose_name_plural = _('Categorías de proyectos')

    def __str__(self) -> str:
        return self.title


class ProjectLanguage(models.Model):
    """
    Programming language used on a project

    Title: Name of language
    """
    title = models.CharField(_("Lenguaje"), max_length=30)

    class Meta:
        verbose_name = _('Lenguaje de proyectos')
        verbose_name_plural = _('Lenguajes de proyectos')

    def __str__(self) -> str:
        return self.title


class ExtLink(models.Model):
    """
    URLS to external site

    title: Name of external site
    link: URL of external site
    """
    title = models.CharField(_("Nombre"), max_length=30)
    link = models.URLField(_("Link"))

    class Meta:
        verbose_name = _('Link externo')
        verbose_name_plural = _('Links externos')

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    """
    Project in which developer has worked or is working

    developer: Foreign key to Developer object
    title: Name of project (in spanish)
    category: Foreign key to ProjectCategory which project belongs
    client: Name of client
    startDate: Project start date
    languages: Programming language/s used in project
    repository: Repository which contains the project sourcecode (optional)
    extLink: URL/S to external site/s related to the project (otional)
    status: Status of project (Production, development, paused or cancelled)
    isActive: Enable/disable the item
    """
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="project", verbose_name=_("Desarrollador"))
    title = models.CharField(_("Nombre"), max_length=30)
    category = models.ForeignKey(ProjectCategory, on_delete=models.RESTRICT, related_name="category", verbose_name=_("Categoría"))
    client = models.CharField(_("Cliente/s"), max_length=60)
    startDate = models.DateField(_("Fecha inicio"))
    languages = models.ManyToManyField(ProjectLanguage, related_name="project_languages", verbose_name=_("Lenguajes utilizados"))
    description = models.TextField(_("Descripción"))
    repository = models.ForeignKey(Repository, on_delete=models.SET_NULL, related_name="repository",blank=True, null=True, verbose_name=_("Repositorio"))
    extLink = models.ManyToManyField(ExtLink, related_name="project_external_links", blank=True, verbose_name=_("Links externos"))
    status = models.CharField(_("Estado"), choices=PROJECT_STATUS_CHOICES, max_length=255)
    isActive = models.BooleanField(_("¿Activo?"), default=True)

    class Meta:
        verbose_name = _('Proyecto')
        verbose_name_plural = _('Proyectos')

    def __str__(self) -> str:
        return self.title


class ProjectImage(models.Model):
    """
    Image that belongs to a project

    project: Foreign key to the project
    image: Image (it will be uploaded on the external server provided)
    altText: Alternative text for HTML purposes
    isFeature: Determines if is the main image of the project
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_images", verbose_name=_("Proyecto"))
    image = models.ImageField(_("Imagen"), upload_to=f"img/projects/", default="img/projects/unavailable.jpg")
    altText = models.CharField(_("Texto alternativo"), max_length=30)
    isFeature = models.BooleanField(_("Portada de proyecto?"), default=False)

    class Meta:
        verbose_name = _('Imagen de proyecto')
        verbose_name_plural = _('Imágenes de proyecto')

    def __str__(self) -> str:
        return self.altText


class Experience(models.Model):
    """
    Developer work experience

    developer: Foreign key to Developer object
    title: Job title
    company: Name of company
    place: Location of position (City, State - Country)
    startDate: Work experience start date
    finishDate: Work experience finish date (optional)
    isPresent: Determines if is currently working on it
    description: Description of position (taks, responsibilities, achivements, etc)
    project: Foreign key to related Project (optional)
    repository: Foreign key to related repository (optional)
    extLink: URL/S to external site/s related to the work experience
    isActive: Enable/disable the item
    """
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="experience", verbose_name=_("Desarrollador"))
    title = models.CharField(_("Título"), max_length=60)
    company = models.CharField(_("Compañía"), max_length=60)
    place = models.CharField(_("Ubicación"), max_length=120, help_text=_("Ej.: Ciudad, Provincia - País"))
    startDate = models.DateField(_("Fecha inicio"))
    finishDate = models.DateField(_("Fecha final"), null=True, blank=True, help_text=_("Opcional"))
    isPresent = models.BooleanField(_("Trabajando actualmente"), default=False)
    description = models.TextField(_("Descripción"))
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    repository = models.ForeignKey(Repository, on_delete=models.SET_NULL, null=True, blank=True)
    extLink = models.ManyToManyField(ExtLink, related_name="experience_external_links", blank=True, verbose_name=_("Links externos"))
    isActive = models.BooleanField(_("¿Activo?"), default=True)

    class Meta:
        verbose_name = _('Experiencia laboral')
        verbose_name_plural = _('Experiencias laborales')

    def __str__(self) -> str:
        return self.title
