from rest_framework import serializers

from {{ devxhub_python.project_slug }}.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        {%- if devxhub_python.username_type == "email" %}
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }
        {%- else %}
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }
        {%- endif %}
