from django.contrib.auth.models import User
from main.users.models import CustomUser

# Function to setup test environment before selenium tests
def setup_test_environment():
    test_base_user1 = User.objects.create_user(username='testuser', first_name='test',  last_name='user', email='test@user.com', password='pass12345')
    test_user1 = CustomUser.objects.create(user=test_base_user1, phone_number='1-234-567-8901', role='user')
    test_base_user2 = User.objects.create_user(username='testadmin', first_name='test',  last_name='admin', email='test@admin.com', phone_number='1-234-567-8901', password='pass12345')
    test_user2 = CustomUser.objects.create(user=test_base_user2, phone_number='1-234-567-8901', role='admin')
