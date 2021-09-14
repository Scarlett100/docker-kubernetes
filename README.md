# Flight_CRUD_App
QA flask application with CRUD functionality


# Contents
 
[Project overview]
[Project Tracking]
[Risk Assesment]


# Project Overview

Our task was to build a Flask application that utilises CRUD functionality. 
In my case I set to build an application pertaining to flights and aeroplanes. 
For my minimum viable product, users would be able to use this application to create their ideal flight, after doing so users would be able to view (read), update and delete their flight entries. 
These flights would be paired with aeroplanes, which also had CRUD functionality. 
If MVP were compelted I would further my application by adding two more tables within my database (Customer and orders) which would then allow users to also complete booking flights on the same web application.
To do this I would first have to make a Trello Kanban board to decipher a realistic approach to the project then begin with my Entity related diagrams and Risk assessment and eventually python, Flask and Jenkins. 
In order to do this, I would need to incorporate and execute my knowledge of Python, Git, Basic Linux, CI, Databases, Cloud Fundamentals and testing.


# Project Tracking

Via the use of Trello a  Kanban board was created and  I began by entering all of the tasks I that had to be completed in order to achieve the minimum viable product. 
Once this was done I began putting label codes on each task following MOSCOW framework. In order to work in an Agile way, and thus provide better results I began planning sprint one.  
I worked by implementing an Agile methodology and followed the MOSCoW framework in order to prioritise and ensure reaching the goal of MVP.
As seen below, my Trello Board evolved over time, the first picture is from the beginning of the project, whilst the second is towards the end of the project.

Below is my board towards the beginning of my project:

![image](https://drive.google.com/uc?export=view&id=1-wlLUZSeGxFm6JPDNJlG6Xbbovk4xLYA)

Below is my board further along in the project.
![image](https://drive.google.com/uc?export=view&id=1SUGIchAK5KAXJ8ERaMZZhuo0i5lpHNay)




# Risk Assessment


The risk assessment enabled me to foresee any problems and how to handle them if they occured.
My risk assessment was a continuous body of work that progressed as I moved further into my applications development. 
For instance, losing data, pushing unnecessary files to git & databases timing out, were all added later in the process . 
The more errors I began to be faced with, the more I was able to foresee further risks. 
As seen below, risks are dated and I included a very simple colour code system for low, medium and high risks and possibilities. 
The risk assessment responses I was able to implement such as restoring code back to its last stable state when the app no longer works were not only time efficient but also evidence of best practice, allowing me to retrace my steps and identify issues.
 

![image](https://drive.google.com/uc?export=view&id=1ah3WD01oCclMt2ERWCIurIHbqBDctqpl)

My Risk Assesment can be accessed [here](https://qalearning-my.sharepoint.com/:x:/g/personal/sstewart_qa_com/ERUyRu7gX9xKo__9xxwu8YwBavBTVAdoKXzBUzWQ2M1NgQ?e=OgSf4j)
# Architecture 
## ERD

 My mvp ERD would contain two tables with the first being Aircraft with a primary key of aircraft_id and the second table being Flights with a primary key of flight_id containing a foreign key of aircraft_id.
The cardinality between the tables was 1 to many.
At first, I had a lot more entries within my table, but it was not necessary for the mvp, which was my priority, so I scaled it down, as visible in the next two images below.

Original ERD:
![image](https://drive.google.com/uc?export=view&id=17nzwoaFxh4q5JLEZ_l3rkAe01vxyJaOh)



Revised ERD:
![image](https://drive.google.com/uc?export=view&id=1gYWLk2SYDR-M5xRYeL4B4EE3_niKChrV)

As aformentioned, if time permitted my intention was to create a an application that allowed customers to also book flights. 
This ERD had four tables and introduced different cardinality such as zero to many.


![image](https://drive.google.com/uc?export=view&id=1cmOqWF6LwDQe8_o241mPK3zsu9qNyRAy)



Below this data was implemented into my models file code.

![image](https://drive.google.com/uc?export=view&id=1RxlxBWXYBcIaOOIB-DOqN0C0xbNmL3ef)

## Databases

Below this data was implemented into my models file code.

![image](https://drive.google.com/uc?export=view&id=1RxlxBWXYBcIaOOIB-DOqN0C0xbNmL3ef)


# CI Pipeline

Within the CI pipeline we used Python, Flask, Jenkins, Git and Trello.
Within python code was written in accordance to the Flask framwork, Pytests unit tests were also carried out within python. 
This code was stored within our repositories that were created, pushed, pulled and cloned from git hub onto our Ubuntu virtual machines.
Once the virtual environment was activated and running from our virtual machine, dependencies were installed to ensure everything could run.
Within our project Jenkins was to be implemented to introduce automation. 
Although I was unable to get Jenkins to produce a complete build, a freestyle project was created intended to be used to fufil a complete build.

![image](https://drive.google.com/uc?export=view&id=1KBi7FM9WE5gzO9eDagnoXP70xI2MGuBq)

# Testing



Testing the CRUD functionality of the application was a key component of the project. 
To do this I wrote unit tests to be able to test create, read, update and delete. 
Tests were also written to ensure the html links were correctly executing.
Eventually I catergorised unit tests by model under 2 classes, because they are catergorised under 2 classes they can be considered intergration tests.

![image](https://drive.google.com/uc?export=view&id=1ivL32andEb7f2dNOlJt9RdFhXKp0EPWl)


Above: two tests within the CRUD testing class for flights. Tests regarding read, update and delete are also grouped here.



As a result of my testing I was able to achieve 85% test coverage as shown on my Pytest coverage report. 

![image](https://drive.google.com/uc?export=view&id=1HYRQBCbnRO_o0zGjH1gEZvch77W5_Uvo)

![image](https://drive.google.com/uc?export=view&id=1QtScUVw6UsQ_3UTAWX81gmq9qyBgYs4-)

The process to get this stage with pycov meant making a sacrifice, 
I found that to increase test coverage I had the issue of tests failing. 
However, I felt it was better to have all tests passing  with slightly less coverage. 
 At one point I went from 80% coverage, to 83% coverage, at the expense of a test failing, as you can see below,.
![image](https://drive.google.com/uc?export=view&id=194ISxxXoCyfDHc5te44Nl2g8LVcSQho_)
Eventually, I achieved 87%. 

![image](https://drive.google.com/uc?export=view&id=1cJtHFFcjWy5DsN6edIBweJ59BYtNg-1k)
However, I soon found that in doing so, the functionality of my application was compromised and an update feature stopped working.

After further research, I made a unit test plan, following a framework found [here](https://codebots.com/crud/how-to-test-CRUD) of all the possibilities that would give more extensive coverage.
After doing so I added one or two tests and was able to find a balance in which my app functionality was no longer compromised, all tests were passed and my coverage was 85% as previously shown.
In hindsight, creating a visual unit test plan prior to beginning unit testing would have allowed me to be more efficient thus enabling me more time to be meticulous and possibly take my coverage even further.
Below is an extract from my unit test plan.

![image](https://drive.google.com/uc?export=view&id=1uxjTXubLoc3gIZ6otIjJOxaYQiLsBddh)


# The app

Within my application, my homepage has a navigation bar that users could access to begin accessing CRUD functionality.


![image](https://drive.google.com/uc?export=view&id=1xltoYf8OPzZ-YlBPbt7zw1E10oDouBIG)

The create a flight page is linked with the foreign key within the flight model; aeroplane_id. 
When creating a flight users can choose from aeroplanes they have previously made to be assigned to their flight. 
Once submitted, a mesage will appear on the homepage with their flight details  

![image](https://drive.google.com/uc?export=view&id=1JMeVJw7CbDBWgQ6GExFrkuw9AWg6yZJ6)

Once submitted, a message will appear on the homepage with their flight or aeroplane details.
To view all their created flights/aeroplanes users have to click  on either "view flights" or "view aeroplanes", where they will then see a list of all entries relating to the corresponding tables.
Also on these pages, is the option for users to update or delete their entry.
![image](https://drive.google.com/uc?export=view&id=1OLi2TVLUXDRTS4Q_LGHNmhefD19-hnc_)



# Areas of improvement

A better working knowledge of HTML:Although not a part of the MVP, an improved working knowledge of HTML would have been very useful and more aesthetically pleasing
Integration Testing within application: Improved reliability and reflection of the CRUD functionality
Included further data from my ERD to my models.py such as Customers and orders.
Add in more “fill in this field” or error messages
Further CRUD functionality, redirect create flights and create aeroplanes to all flights and all aeroplanes, asthetically and design wise would make application slight smoother.
Extensive unit test planning: After planning my unit tests, I received a 10% increase in my coverage. Even though only a few of my unit test plans were used it provided clarity and efficiency.
Increased coverage: By adding utilising more of my planned tests coverage could be improved from 85% to at least 90%. 
Succesful Utilised Automation through Jenkins.
Debug issue regarding RDS dataabase connection.




# Closing thoughts

In future, I am confident that I have a good foundation and working knowledge that would enable me to create another Flask Crud application and build on my knowledge. 
Combining my knowledge of Agile, databases, python, git and Visual Studio code enabled me to produce a Flask application in which users were able to access all CRUD functionality. 
As aforementioned, in further improvements full grasping of Jenkins would be ideal and is something that I intend to implement. 
To conclude, as a beginner, this project has been wonderful not only as a learning experience in how to produce an MVP and plan towards a stretch goal but also how to assess our strengths and areas for improvement.

# References
    https://codebots.com/crud/how-to-test-CRUD
    https://www.w3schools.com/html/html_tables.asp

# Acknowledgements
    I would like to acknowledge my tutors at QA for their teaching of technolodgies nescessary to complete this task.


# Licenses
