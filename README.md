This is a simple flask app to practice cascade deleting in SQLalchemy. Data is stored in Postgres.


### Features:
+ **Users** can add thier profile to the db. 
+ They can also add **Options** which can be anyting, in the example gifs, **Options** are foods.
+ **Users** can associate themselves with **Options**, creating **User_options**.
+ **Users** can **Comment** on thier **User_options**.
+ Deleting a **User_option** deletes all **Comments** associated with that **User_option**, but not the **Option**.
+ Deleting an **Option** deletes all **User_options** associated with that **Option** and all **Comments** associated with that **Option**.

![gif1](https://github.com/trabnett/flask-cascade-delete/blob/master/static/cascade_delete1.gif)
![gif2](https://github.com/trabnett/flask-cascade-delete/blob/master/static/cascade_delete2.gif)