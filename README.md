# web_application_project
**Backend**
In terminal   **pip install -r requirements.txt**
Then **python manage.py runserver**   


**Login by admin**<br>
**User name: admin**<br>
**Password:admin123**<br>
I still want to keep the client user, admin uses django's absuser way, and is separating them. So i use JWT authentication. And I also use throttle to protect back-end services

**Frontend**
In terminal  **npm install** and **npm run start** 

**Deploy front-end**<br>
Keep running the frontend and backend termianl <br>
in the frontend open a new terminal window, run **.\ngrok.exe http 3000**,Maybe not 3000,it's depend on your frontend localhost
Then get the link from Forwarding like https://xxxx-xxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx.ngrok-free.app/ Click it and run,you can also open on the phone with this link