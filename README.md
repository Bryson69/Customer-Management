
<p align="center">
   <h1>Customer Management</h1><br>
    <br>
     <img src="https://forthebadge.com/images/badges/made-with-python.svg" >
    <br>
</p>


### Live Site [Customer Management](https://crm1-bryson.herokuapp.com/) 

## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes, 
1. **clone** this repository 
   ``` 
   git clone https://github.com/Bryson69/Customer-Management
   ```
2. Set up a Python development environment that includes; Python, **pip** & **a virtual environment** 
   ```bash
   $ python3.6 -m venv --without-pip virtual

   $ source virtual/bin/activate

   (virtual) $ curl https://bootstrap.pypa.io/get-pip.py | python
   ```
3. Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='rdtfyguihjohucbdsjnc'
DEBUG=True
DB_NAME='tribune'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

### Prerequisites

1. Install project *****dependencies*****
   ```
    (virtual) $ pip install -r requirements.txt
    ```
* See deployment for notes on how to deploy the project on a live system.


### Installing

1.  To get a development env running, use the **.env.example** file to create your own **.env** file.
2.  Create a **postgres** db and add the credentials to .env file
```
(virtual)$ psql
pc-name=#  CREATE DATABASE <name>;
```
3.  Apply initial migrations
```sh 
(virtual) $ python manage.py migrate 
```
4. Make migrations to your database
```sh
(virtual) $ python manage.py makemigrations application
(virtual) $ python manage.py migrate
```
5. Create admin account
```
(virtual) $ python manage.py createsuperuser
```
6.  Start development server
```
 (virtual) $ python3 manage.py runserver
 ```


#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

# Support and Contacts
In case You have any issues using this code please do no hesitate to get in touch with me through brysonmundia@gmail.com or leave a comment here on Github.

## Known Bugs
None so far.

## Built With

* [Django 3.1](https://www.djangoproject.com/) - The web framework used
* [Heroku](https://www.heroku.com/platform) -  Deployment platform
* [Python3.6](https://www.python.org/) - Backend logic
* [Postresql](https://www.postgresql.org/) - Database system


### License
**[MIT](./LICENSE)** (c) 2020 **[Bryson Mundia]()**
