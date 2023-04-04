from django.urls import path, re_path

from . import views

app_name = "portfolio"

urlpatterns = [
    # Home (Just for testing)
    path('', views.home, name='home'),

    # Developer
    re_path(r'^developer$', views.DeveloperList.as_view(), name="developer"),
    re_path(r'developer/(?P<pk>[0-9]+)$', views.DeveloperDetail.as_view()),
    
    # Title
    re_path(r'^title$', views.TitleList.as_view(), name="title"),
    re_path(r'title/(?P<pk>[0-9]+)$', views.TitleDetail.as_view()),
    
    # SocialLink
    re_path(r'^social_link$', views.SocialLinkList.as_view(), name="social_link"),
    re_path(r'social_link/(?P<pk>[0-9]+)$', views.SocialLinkDetail.as_view()),
    
    # Language
    re_path(r'^language$', views.LanguageList.as_view(), name="language"),
    re_path(r'language/(?P<pk>[0-9]+)$', views.LanguageDetail.as_view()),
    
    # Skill
    re_path(r'^skill$', views.SkillList.as_view(), name="skill"),
    re_path(r'skill/(?P<pk>[0-9]+)$', views.SkillDetail.as_view()),
    
    # Framework
    re_path(r'^framework$', views.FrameworkList.as_view(), name="framework"),
    re_path(r'framework/(?P<pk>[0-9]+)$', views.FrameworkDetail.as_view()),
    
    # Repository
    re_path(r'^repository$', views.RepositoryList.as_view(), name="repository"),
    re_path(r'repository/(?P<pk>[0-9]+)$', views.RepositoryDetail.as_view()),
    
    # Education
    re_path(r'^education$', views.EducationList.as_view(), name="education"),
    re_path(r'education/(?P<pk>[0-9]+)$', views.EducationDetail.as_view()),
    
    # ProjectCategory
    re_path(r'^project_category$', views.ProjectCategoryList.as_view(), name="project_category"),
    re_path(r'project_category/(?P<pk>[0-9]+)$', views.ProjectCategoryDetail.as_view()),
    
    # ProjectLanguage
    re_path(r'^project_language$', views.ProjectLanguageList.as_view(), name="project_language"),
    re_path(r'project_language/(?P<pk>[0-9]+)$', views.ProjectLanguageDetail.as_view()),
    
    # ExtLink
    re_path(r'^external_link$', views.ExtLinkList.as_view(), name="external_link"),
    re_path(r'external_link/(?P<pk>[0-9]+)$', views.ExtLinkDetail.as_view()),
    
    # Project
    re_path(r'^project$', views.ProjectList.as_view(), name="project"),
    re_path(r'project/details/(?P<pk>[0-9]+)$', views.ProjectDetail.as_view()),
    re_path(r'project/dev$', views.DevProjectList.as_view(), name="dev_project"),
    re_path(r'project/pro$', views.ProProjectList.as_view(), name="pro_project"),
    re_path(r'project/pau$', views.PauProjectList.as_view(), name="pau_project"),
    re_path(r'project/can$', views.CanProjectList.as_view(), name="can_project"),
    
    # ProjectImage
    re_path(r'^project_image$', views.ProjectImageList.as_view(), name="project_image"),
    re_path(r'project_image/(?P<pk>[0-9]+)$', views.ProjectImageDetail.as_view()),
    
    # Experience
    re_path(r'^experience$', views.ExperienceList.as_view(), name="experience"),
    re_path(r'experience/(?P<pk>[0-9]+)$', views.ExperienceDetail.as_view()),
    
]
