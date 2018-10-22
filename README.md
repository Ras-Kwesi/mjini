# MJINI
A web application where users create profile linked to a community through which they can make posts, and interact with other Users and their businesses within a comunity.

------------------------------------------------------------------------
## BY: [Ras Kwesi](https://github.com/Ras-Kwesi)

## User Requirements

1. Create profile and modify and access profile.
2. Signup to a Community.
3. View community posts on home page.
4. Create Business posts and View social services.
5. Search for business and their details.
6. Create new Neigbour hoods and be the Administrator.



## Models
### Post 
* Properties: Title, Description, Hood FK, Poster FK.

### Profile 
* Properties: Profile Picture, Bio, location, Django User Relationship, Contact

### Business
* Properties: Name, Owner FK , Description, Number. Locale FK

### Hood
* Properties: Name, Bio


## Admin Dashboard
Use django admin to post photos to the database and manage the photos

## Setup

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3

### Cloning the repository
```bash
git clone https://github.com/Ras-Kwesi/mjini.git && cd mjini
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip install -r requirements.txt
```

### Prepare environmet variables
Create a .env file and add the following configutions to it
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME=#database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running Tests
```bash
python manage.py test
```

### Running the server 
```bash
python manage.py runserver
```
## Contributing

- Git clone [https://github.com/Ras-Kwesi/mjini.git](https://github.com/Ras-Kwesi/mjini.git) 
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

### Deploying to heroku
Refer to this guide: [deploying to heroku](https://github.com/Ras-Kwesi/Deployment_to_heroku_django)
Set the configuration to production mode

## Live Demo

The web app can be accessed from the following link: 
[Website Ranker](https://mjini.herokuapp.com/)


## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://docs.djangoproject.com/en/1.11/)
* [Heroku](https://heroku.com)


## License
MIT License

Copyright(c) 2018

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.