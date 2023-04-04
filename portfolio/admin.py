from django.contrib import admin

from .models import (
    Developer,
    Education,
    Experience,
    ExtLink,
    Framework,
    Language,
    Project,
    ProjectCategory,
    ProjectImage,
    ProjectLanguage,
    Repository,
    Skill,
    SocialLink,
    Title,
)


admin.site.register([
    Experience,
    ExtLink,
    Repository,
    Education,
    ProjectCategory,
    ProjectLanguage,
])


class DeveloperLanguageInline(admin.TabularInline):
    model = Language


class DeveloperSkillInline(admin.TabularInline):
    model = Skill


class DeveloperSocialLinkInline(admin.TabularInline):
    model = SocialLink


class DeveloperTitleInline(admin.TabularInline):
    model = Title


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    inlines = [
        DeveloperLanguageInline,
        DeveloperSkillInline,
        DeveloperSocialLinkInline,
        DeveloperTitleInline,
    ]


class SkillFrameworkInline(admin.TabularInline):
    model = Framework


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    inlines = [
        SkillFrameworkInline,
    ]


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectImageInline,
    ]
