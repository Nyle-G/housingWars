Our project has two primary parts, the frontend and backend.

Frontend:

The design of the website was done in HTML and utilized bootstrap and Jinja.

In structuring the html files, we wrote up a layout.html file that acted as a template upon which every other html file was based off of. That is, you cannot access layout.html
in our web application, but every single accessible html file extends layout.html.

LAYOUT
In the layout file, we included tags like the meta tag, which would autoformat our webpage across all devices and screens, and implemented bootstrap, which we used throughout our code to format our webpage.
Additionally, we implemented a universal navigation bar in layout at the top of the webpage through which users could navigate to different pages. In the navigation bar, we utilize Jinja
if statements to test what items would be present in the navbar depending on if a user was signed in or not. We include a main block through Jinja in the main tag of layout that would allow each html file to add elements to the main part of the webpage.
We also implemented a footer item in layout.html that would be present across every html page.

REGISTER
Register.html extends layout.html and includes a form with form-groups that allow users to enter a username, a password, and to confirm their password. The python application will check these inputs and utilize SQL to register the user.

LOGIN
Login.html extends layout.html and includes a form with form-groups that allow users to input a username and a password. The python application will check if the inputs in this form match a real user and will then log them in.

INDEX
The index.html file is the main page of the web application after users login. Users can see current house rankings and breakdowns on the index page.
Index.html extends layout.html and includes two tables, one that shows the overall rankings of the houses and their rankings of basic categories, and another that shows more detailed breakdowns of house ratings.
Tables entries are primarily created with the help of Jinja: rankings and ratings are calculated and sent in order by the python app and then formatted through Jinja loops and conditionals into entries in html tables.
We also used the jumbotron elements in bootstrap to format titles for each of the tables.

RANK
Rank.html extends layout.html and allows users to input their ratings for houses of their choice. It includes a form that allows users to select which of the twelve houses they want to rate (by use of the select tag in html)
and input integer rankings between 1 and 10, inclusive, for six categories. The submit button on the page allows users to submit their page, and the python app will log those submissions. Jumbotrons are used again to design headings.

HOUSE BIOS
houseBios.html extends layout.html and consists of a massive accordion tag that holds numerous cards, as per bootstrap. Each of these cards include a picture of their house via the img tag as well as basic info regarding the house done 
through a simple table.
 
APOLOGY
apology.html extends layout.html and simply consists of a image that takes input and returns a picture with those inputs detailing an error. This is done by the python web app whenever an error is detected in a user's interaction with the website.


Backend:

On the SQL side of thing, there are three primary tables:
1. Users
2. Rankings
3. Ranking

The users table stores all the usernames and hashed passwords of the users.
The ranks table stores all the inputted ranks by users for each of the houses and their respective subcatagories.
The ranking table reflects the actual rankings of the 12 houses, alonside their overall score and average scores in the subcatagories.

The different routes:

REGISTER:

The register funcionality was handled via python and the SQL database titled "users".
The python if statements check to make sure that:
1. A username was entered
2. The username doesn't already exist
2. A password was entered
3. A password confirmation was entered
3. The entered passwords matched

The username and a hash of the password is then entered into the SQL database.

LOG IN:

The log in funcionality was handled via python and the SQL database titled "users".
The python if statements check the following:
1. A username was entered
2. A password was entered

The database is then queried to make sure the username exists, and that the entered password
matches the entered username. If all these conditions are true, the user is logged in and
taken to the homepage of the site.

INDEX:

Index, or the homepage method, handles the back of the data logic.
It is responsible for finding the average values of the six subcatagories
alongside the overall average value, entering the values in the SQL database,
and then updating the site with the updated information and rankings of the houses.

Here is how that is handled:

Each of the twelve house has the following commands:
1. The method first checks to make sure that there are rankings inputted for the given house via an if statement and SQL query on the rank table.
2. It then calculates and stores the sum of each of the six factors for the given house usinng a SQL query on the rank table.
3. It then calculates and rounds the averagae of each of the six subcategories by dividing by the total number of rankings.
4. The average of the six values is then computed and rounded and stored as the overall value for the given house.
5. The averages and the overall values are then inputted into a SQL table titled "rankings" by updating the values for the respective house.

The process is then repeated for the remaining houses.

The rankings are then stored in a variable by executing a SQL query on the rankings table that also orders the rows from
greatest to least in the order of their overall scores (to give a ranking order), and this is then passed to the webpage
and reflected in the webpage tables using a Jinja for loop.

RANK:

The rank method takes the values entered by the users and enters it into the ranks database.
Here is how that is executed:
1. Upon entering a value into the table, the six values are stored in python variables using request.form.get
2. The values are then inputted into the ranks database using a SQl command.
3. The updated value is then reflected when the index method is called and rankings are recalculated and updated.