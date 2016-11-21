# wfh-api
Rest-APIs for WorkFromHomeManager Application

#Steps to use these APIs
1. Clone the repo.
2. change directory to this repo - cd <your path>/wfh-api
3. Initialize virtualenv - source /bin/activate
    You will see (wfh-api) in your terminal.
4. cd wfh
5. run the server - python manage.py runserver (server will start on 8000 port).
    You can start the server on any port. Use python manage.py runserver <your port>
6. Go to browser and type 127.0.0.1:8000/docs (for default port)
    You can see all available APIs available.
    Checkout responses available.
    Use these Endpoint explicitely like (In new tab)-
      127.0.0.1:8000/api/team - 
      Similarly for all other APIs.
Don't Use Live API Endpoint available in /docs as its still in Beta.
7. Use admin dashboard to add data. 127.0.0.1:8000/admin
    Use credentials tushar/Admin@123

Happy Coding!....
