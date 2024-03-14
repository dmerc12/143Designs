from django.contrib.auth.models import User
from main.users.models import CustomUser

# Function to clean up test environment after selenium tests
def cleanup_test_environment():
    User.objects.all().delete()
    CustomUser.objects.all().delete()
