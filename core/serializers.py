from rest_framework import serializers
from .models import Job, JobApplication, JobTitle


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    organisation = serializers.CharField(source='organisation.name')
    title = serializers.CharField(source='title.title')

    class Meta:
        model = Job
        fields = '__all__'


class JobApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(many=False)

    class Meta:
        exclude = ('seeker', )
        model = JobApplication
