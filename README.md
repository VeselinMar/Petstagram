# Petstagram

Petstagram is a Django web application reminding a lot of FurryBuddies but better in every way. 
Users can create, edit, and delete posts, and view details of other pets in the community.

# Installation

### 1. Clone the repo
   
  ```terminal

    git clone https://github.com/VeselinMar/Petstagram.git

  ```

### 2. Open the project


### 3. Install dependencies
 
   ```terminal
   
     pip install -r requirements.txt
  
   ```

### 4. Change DB settings in settings.py

  ```py
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "your_db_name",
            "USER": "your_username",
            "PASSWORD": "your_pass",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
  ```

### 5. Run the migrations

  ```terminal

    python manage.py migrate

  ```

### 6. Run the project

  ```terminal

    python manage.py runserver

  ```

## Images
![Registration](static/images/screenshots/Screenshot%20from%202024-11-17%2018-15-12.png)
![Dashboard](static/images/screenshots/Screenshot%20from%202024-11-17%2018-15-45.png)
![AddPet](static/images/screenshots/Screenshot%20from%202024-11-17%2018-15-59.png)
![AddPhoto](static/images/screenshots/Screenshot%20from%202024-11-17%2018-16-11.png)
