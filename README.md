# curd_practical
Curd Practical Using Django and Django REST

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)


This is a simple CURD operations Project, made using Django and Django REST, 
Can be used as web as well as API Way.


## Installing the Packages from the Ubuntu Repositories

- To begin the process, we’ll download and install all of the items we need from the Ubuntu repositories. We will use the Python package manager pip to install additional components a bit later.
- We need to update the local apt package index and then download and install the packages. The packages we install depend on which version of Python your project will use.

    ```bash
    $ sudo apt update

    $ sudo apt install python3-pip python3-dev libpq-dev 
    ```

------------

## Setting Up and Running Project

- For the sake of simplicity SQLite Database is used.
- Take clone from the project Repo.
- Open Terminal at Project base directory, that would be directory where `manage.py` is located.
- Create a Virtual Environment using command  `python3 -m venv venv(your_desired_enviroment_name)`
- Install required packages using command `pip install -r requirements.txt`
- The Repo already has a SQLite Database file with One SuperUser Created. You can use that DB or Create a new one for yourself.
- To Run Project use command `python manage.py runserver`
- If you Don't get any errors, you have successfully run project, goto browser and type `localhost:8000` you should see the project.

## Setting Up and Running Project Using Docker For X86 Architecture System (Linux, Windows, etc)(Intel/AMD Based Processors)
- Install Docker on your system 
- Take Project build pull from Docker Hub using Command : `docker pull shubhamdevgan/curd_demo:x86_64_arch`
- Run Docker Image using Command : `docker run -p 8000:8000 shubhamdevgan/curd_demo:x86_64_arch`
- If you Don't get any errors, you have successfully run project, goto browser and type `localhost:8000` you should see the project.

## Setting Up and Running Project Using Docker For ARM Architecture System (Apple M1 Processor based systems)
- Install Docker on your system 
- Take Project build pull from Docker Hub using Command : `shubhamdevgan/curd_demo:arm_arch`
- Run Docker Image using Command : `docker run -p 8000:8000 shubhamdevgan/curd_demo:arm_arch`
- If you Don't get any errors, you have successfully run project, goto browser and type `localhost:8000` you should see the project.

## Scalling the Project
- Project can be scalled using Multi-Container Architecture using Docker Container by Using and Container orchestration technology such as Kubernetes, AWS EKS, AWS ECS



## POSTMAN COLLECTION CAN BE FOUND AT
- https://www.getpostman.com/collections/59c91f47ae6acbf79e68
