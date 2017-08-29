Technologies :
django
python
Mysql
Html
css
bootstrap
angularJS


# dj-devrsc
#create virtual environment
virtualenv djenv

# activate virtual env

source djenv/bin/active

# go to project directory
cd rscproject

# install requirements
pip install -r requirements.txt

# if any error as "No matching distribution found for requirements.txt"

pip install --upgrade -r requirements.txt

#run the server
python manage.py runserver
