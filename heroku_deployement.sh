mkdir bottle_heroku
cd bottle_heroku/
virtualenv --no-site-packages env
source env/bin/activate
pip install bottle gevent
pip freeze > requirements.txt
 
chmod a+x app.py
 
echo 'web: app.py' > Procfile
echo 'env/' > .gitignore
 
git init
git add .
git commit -m "Initial commit"
 
heroku create
git push heroku master