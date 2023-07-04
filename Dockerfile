# start from an official image
FROM python:3.10.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# USER devops
# arbitrary location choice: you can change the directory
# RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install our dependencies
COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

# RUN pipenv shell
# RUN python manage.py makemigrations --no-input 

RUN python manage.py migrate --no-input 

RUN python manage.py collectstatic --no-input -v 2

# expose the port 8000
EXPOSE 8000




# define the default command to run when starting the container
# CMD ["gunicorn", "--chdir", "core", "--bind", ":8000", "core.wsgi:application", "--reload"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
