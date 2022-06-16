# travel_bucket_list_app_project
My first project at CodeClan! It was designed to consolidate and expand our knowledge of Python, test driven development, web programming with RESTful routes and MVC, Flask, and interacting with a PostgreSQL database (CRUD).

Over six days, I was tasked with building a simple web app using only HTML/CSS, Python, Flask, PostgreSQL, and psycopg. The web app would allow the user to create and track their travel adventures. They will be able to add destinations and save them to a database, be able to view all the destinations they have on the list, and can update the destination as visited.

## MVP (Minimum Viable Product):
* The app should allow the user to track `Country`s and `City`s they want to visit and those they have visited.
* The user should be able to create and edit `Country`s.
* Each `Country` should have one or more `City`s to visit.
* The user should be able to create and delete `Citys`.
* The app should allow the user to mark destinations as visited or not.

## Possible Extensions:
* Add sights to see at the destination `City`s.
* Be able to filter `City`s based on whether they have been visited.
* Allow the user to search for a destination by city name, region, or continent 

## Project Setup:
In Teminal:
1. Type in `createdb bucket_list_tracker` to create the database
2. Run `psql -d bucket_list_tracker -f db/bucket_list_tracker.sql` to create the tables for the database
3. Populate the database by running `python3 console.py`
4. CTRL + C to quit pub
5. Type `flask run`
6. Enter `http://127.0.0.1:5000` in your web browser or hovering over  `Running on http://127.0.0.1:5000 (Press CTRL+C to quit)`, hold command + click on server to open the web app
