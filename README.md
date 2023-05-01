# Book-exchanging-system

### A robust system that helps in exchanging of books within a community of members, so that a necessity of a member towards a book is at most satisfied.

 A community consisting of huge members might have many books of different genres and would be just occupying extra spaces. A member in a
 community might require a book where another member in the same might have it and could be anonymous. The idea is to develop a portal that 
 can create connections between the community members and exchange information about the books. The community members should be able to list 
 the books they are willing to exchange with others in the forum while the database stores the information about the books listed by every 
 user. Members would be able to search for the required books and based on availability, contact information would be provided. Private discussion 
 can be done between the members of the community, and exchanges can be made.

# Getting Started with Book-Exchanging-System

This project was created using [Flask](https://flask.palletsprojects.com/en/2.2.x/) and
 <p align="center">
  <a href="#">
    <img src="https://skillicons.dev/icons?i=html,css,js,flask,sqlite,git,vscode,github" />
  </a>
</p>

## Running the Server

In the project directory, you can run:
```
gunicorn -w 4 --bind 0.0.0.0:6100 main:gunicorn_app
```

Runs the app in the development mode.\
Open <http://localhost:6100/> to view it in your browser.

## Missing Modules

Recommended to create virtual environment and install modules from requirements.txt using:
```
pip install -r requirements.txt
```
