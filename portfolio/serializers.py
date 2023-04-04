from rest_framework import serializers

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


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = (
            "id",
            "firstName",
            "lastName",
            "openToWork",
            "jobTitle",
            "phone",
            "email",
            "residence",
            "photo",
            "about",
            "aboutShort",
            "cvEsp",
            "cvEng",
        )


class TitleSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer()

    class Meta:
        model = Title
        fields = (
            "id",
            "developer",
            "title",
        )


class SocialLinkSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer()

    class Meta:
        model = SocialLink
        fields = (
            "id",
            "developer",
            "title",
            "icon",
            "link",
            "isActive",
        )


class LanguageSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer()

    class Meta:
        model = Language
        fields = (
            "id",
            "developer",
            "title",
            "proficiency",
            "isActive",
        )


class SkillSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer()

    class Meta:
        model = Skill
        fields = (
            "id",
            "developer",
            "title",
            "proficiency",
            "isActive",
        )


class FrameworkSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()
    class Meta:
        model = Framework
        fields = (
            "id",
            "skill",
            "title",
            "icon",
            "isActive",
        )


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = (
            "id",
            "title",
            "link",
            "readmeLink",
        )


class EducationSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer()
    repository = RepositorySerializer()

    class Meta:
        model = Education
        fields = (
            "id",
            "developer",
            "title",
            "place",
            "link",
            "startDate",
            "finishDate",
            "isPresent",
            "description",
            "certificate",
            "repository",
            "isActive",
        )


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = (
            "id",
            "title",
        )


class ProjectLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLanguage
        fields = (
            "id",
            "title",
        )


class ExtLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtLink
        fields = (
            "id",
            "title",
            "link",
        )


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = (
            "id",
            "project",
            "image",
            "altText",
            "isFeature",
        )


class ProjectSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer()
    category = ProjectCategorySerializer()
    languages = ProjectLanguageSerializer(many=True)
    project_images = ProjectImageSerializer(many=True)
    repository = RepositorySerializer()
    extLink = ExtLinkSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "developer",
            "title",
            "category",
            "client",
            "startDate",
            "languages",
            "description",
            "project_images",
            "repository",
            "extLink",
            "status",
            "isActive",
        )


class ExperienceSerializer(serializers.ModelSerializer):
    developer = DeveloperSerializer()
    project = ProjectSerializer()
    repository = RepositorySerializer()
    extLink = ExtLinkSerializer(many=True)

    class Meta:
        model = Experience
        fields = (
            "id",
            "developer",
            "title",
            "company",
            "place",
            "startDate",
            "finishDate",
            "isPresent",
            "description",
            "project",
            "repository",
            "extLink",
            "isActive",
        )
