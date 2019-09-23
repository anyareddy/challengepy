# Challengepy - Server Challenge

For this challenge I have written the backend for a version of "Penn Club Review".

## How I stored my information

For my Clubs class I used a static variable that is a list of all Club objects that have been created in the Club class. I also stored all the usernames in another static variable. My user class also stores all the User objects that have been created and all the usernames created in two separate static variables.

## Club Object

## User Object

## Other features that I added
I included a route '/api/joinClub' that uses a POST method to allow users to join a club. When they join a club then their email gets added to club members. I also included a route '/api/members/<club>' that uses a GET method to allow users to request all the emails of members in a club. My purpose for this is to allow users on the website a way to contact members of certain clubs if they have any questions. This means that users will join a club if they would be open to being contacted by potential new club members. This feature could instead potentially be used for adding people to a ListServ, etc. 

