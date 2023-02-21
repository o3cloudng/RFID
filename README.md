# RFID Attendance Monitoring System


## Steps to deploy to Heroku using heroku cli

* Install Heroku cli

``` 
heroku login 
```

```
heroku create
```
This will show us the link to our heroku website 

(https://limitless-depths-73924.herokuapp.com/ )


and Git repo for heroku 

(https://git.heroku.com/limitless-depths-73924.git)

```
heroku git:remote -a limitless-depths-73924
```

Generate requirements.txt file using
```
pip freeze > requirements.txt
```
Create Procfile 

``` web: gunicorn core.wsgi ```


Then run cmd to text
```
heroku local
```