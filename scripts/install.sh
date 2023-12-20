# update package lists
sudo apt update
# install python
sudo apt install python3 python3-pip
# install git
sudo apt install git
# install project from github
git clone https://github.com/dmerc12/143Designs.git
# change into project
cd 143Designs
# create virtual environment
python3 -m venv venv
# activate virtual environment
source venv/bin/activate
# install django and other dependencies
pip install django crispy-bootstrap5 crispy-forms
# change into django project
cd version/
# create database migrations
python3 manage.py makemigrations
# migrate database
python3 manage.py migrate
# take user input for admin username
read -p "Enter admin username: " admin_username
echo
# take user input for admin email
read -s -p "Enter admin email: " admin_email
# take user input for admin password
read -s -p "Enter admin password: " admin_password
echo
# take user input for admin password confirmation
read -s -p "Confirm admin password: " admin_password_confirmation
echo
# check if passwords match
if ["$admin_password" != "$admin_password_confirmation"]; then
    echo "Passwords do not match. Exiting."
    exit 1
fi
# create super user using admin credentials with admin input
python3 manage.py createsuperuser --username "$admin_username" --email "$admin_email" --password "$admin_password" --admin_password_confirmation "$admin_password_confirmation"
# run server
python3 manage.py runserver
# run unit tests
# run end to end tests
