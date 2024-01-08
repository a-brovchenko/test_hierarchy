# test_hierarchy
To run the application in the app folder create an .env file and place the following code
```
# django 
SECRET_KEY='django-insecure-@0g8(k)n%=#c6)%@-j^sxk#w5o@8mp)wghbr2z0^xctsg5xz_q'

#db
DB_HOST='127.0.0.1'
DB_NAME='workers'
DB_USER='root'
DB_PASSWORD='password'
```
By default, when the container starts, the database will be filled with 3280 records, if there is a need to increase the number of records, change the value of the variable numb in the file seed.py

In the project root enter the command

```
docker-compose up -d
```
It will take some time to launch the application

After this you can access the working Django container under localhost:8000 and the database under localhost 8081