# Challengepy - Server Challenge

For this challenge I have written the backend for a version of "Penn Club Review". All classes and routes are stored on the index.py file.

## How I stored my information

For my Clubs class I used a static variable that is a list of all Club objects that have been created in the Club class. I also stored all the usernames in another static variable. My user class also stores all the User objects that have been created and all the usernames created in two separate static variables.

## Club Class
The club object includes these instance variables: a club name, a description of the club, a list of club tags, the number of favorites a club has, and the user emails that have joined the club. The class also includes a method that outputs all the club names and the number of favorites that each has. This class also has two different methods to update the number of favorites a club has and to update the users in a club.

## User Class
The user object includes these instance variables: a name, a username, an email, a users graduation year, club names that a user has favorited, a password, and clubs that they've joined. There is also a method that outputs all the profile information of a user. It includes all instance variable information except for a user's password.

## Extra features that I added
I included a route '/api/joinClub' that uses a POST method to allow users to join a club. When they join a club then their email gets added to club members. I also included a route '/api/members/<club>' that uses a GET method to allow users to request all the emails of members in a club. My purpose for this is to allow users on the website a way to contact members of certain clubs if they have any questions. This means that users will join a club if they would be open to being contacted by potential new club members. This feature could instead potentially be used for adding people to a ListServ, etc. 
  
## Routes Created given by challenge
I created all routes that were given in the challenge. I also included the bonus feature of allowing club information to be updated with the POST /api/clubs route.
