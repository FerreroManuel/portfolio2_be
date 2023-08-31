from django.shortcuts import render

from rest_framework import generics

from portfolio.models import (
    Developer,
    Title,
    SocialLink,
    Language,
    Skill,
    Framework,
    Repository,
    Education,
    ProjectCategory,
    ProjectLanguage,
    ExtLink,
    Project,
    ProjectImage,
    Experience,
)
from portfolio.serializers import (
    DeveloperSerializer,
    TitleSerializer,
    SocialLinkSerializer,
    LanguageSerializer,
    SkillSerializer,
    FrameworkSerializer,
    RepositorySerializer,
    EducationSerializer,
    ProjectCategorySerializer,
    ProjectLanguageSerializer,
    ExtLinkSerializer,
    ProjectSerializer,
    ProjectImageSerializer,
    ExperienceSerializer,
)


# Home (Just for testing)
def home(request):
    return render(request, 'home.html')

# Developer
class DeveloperList(generics.ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class DeveloperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


# Title
class TitleList(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class TitleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


# SocialLink
class SocialLinkList(generics.ListCreateAPIView):
    queryset = SocialLink.objects.filter(isActive=True).order_by('id')
    serializer_class = SocialLinkSerializer


class SocialLinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialLink.objects.all().order_by('id')
    serializer_class = SocialLinkSerializer


# Language
class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.filter(isActive=True).order_by('-proficiency')
    serializer_class = LanguageSerializer


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all().order_by('-proficiency')
    serializer_class = LanguageSerializer


# Skill
class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.filter(isActive=True).order_by('-proficiency')
    serializer_class = SkillSerializer


class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all().order_by('-proficiency')
    serializer_class = SkillSerializer


# Framework
class FrameworkList(generics.ListCreateAPIView):
    queryset = Framework.objects.filter(isActive=True).order_by('id')
    serializer_class = FrameworkSerializer


class FrameworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Framework.objects.all().order_by('id')
    serializer_class = FrameworkSerializer


# Repository
class RepositoryList(generics.ListCreateAPIView):
    queryset = Repository.objects.all().order_by('id')
    serializer_class = RepositorySerializer


class RepositoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Repository.objects.all().order_by('id')
    serializer_class = RepositorySerializer


# Education
class EducationList(generics.ListCreateAPIView):
    queryset = Education.objects.filter(isActive=True).order_by('-finishDate')
    serializer_class = EducationSerializer


class EducationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all().order_by('-finishDate')
    serializer_class = EducationSerializer


# ProjectCategory
class ProjectCategoryList(generics.ListCreateAPIView):
    queryset = ProjectCategory.objects.all().order_by('id')
    serializer_class = ProjectCategorySerializer


class ProjectCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectCategory.objects.all().order_by('id')
    serializer_class = ProjectCategorySerializer


# ProjectLanguage
class ProjectLanguageList(generics.ListCreateAPIView):
    queryset = ProjectLanguage.objects.all().order_by('id')
    serializer_class = ProjectLanguageSerializer


class ProjectLanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectLanguage.objects.all().order_by('id')
    serializer_class = ProjectLanguageSerializer


# ExtLink
class ExtLinkList(generics.ListCreateAPIView):
    queryset = ExtLink.objects.all()
    serializer_class = ExtLinkSerializer


class ExtLinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtLink.objects.all()
    serializer_class = ExtLinkSerializer


# Project
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.filter(isActive=True).order_by('startDate')
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all().order_by('startDate')
    serializer_class = ProjectSerializer


class DevProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.filter(status='DEV')
    serializer_class = ProjectSerializer


class ProProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.filter(status='PRO')
    serializer_class = ProjectSerializer


class PauProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.filter(status='PAU')
    serializer_class = ProjectSerializer


class CanProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.filter(status='CAN')
    serializer_class = ProjectSerializer


# ProjectImage
class ProjectImageList(generics.ListCreateAPIView):
    queryset = ProjectImage.objects.all().order_by('-isFeature')
    serializer_class = ProjectImageSerializer


class ProjectImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectImage.objects.all().order_by('-isFeature')
    serializer_class = ProjectImageSerializer


# Experience
class ExperienceList(generics.ListCreateAPIView):
    queryset = Experience.objects.filter(isActive=True).order_by('-finishDate').order_by('-startDate')
    serializer_class = ExperienceSerializer


class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all().order_by('-finishDate').order_by('-startDate')
    serializer_class = ExperienceSerializer
