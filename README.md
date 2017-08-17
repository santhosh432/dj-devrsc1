# dj-devrsc
#create virtual environment
virtualenv djenv

# activate virtual env

source djenv/bin/active

# got o project directory
cd rscproject

# install requirements
pip install requirements.txt

# if any error as "No matching distribution found for requirements.txt"

pip install --upgrade -r requirements.txt

#run the server
python manage.py runerver
