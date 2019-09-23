from flask import Flask, request, jsonify
from flask import abort
import json
from scraper import * # Web Scraping utility functions for Online Clubs with Penn.
app = Flask(__name__)

class Club:
    #List of all clubs created
    all_clubs = []
    #List of all club names
    all_names = []

    #Intialize with a club name, description, list of tags, number of facvorites, and user emails that have joined the club
    def __init__(self, name, description, tags, favorites, users):
        self.name = name
        self.description = description
        self.tags = tags
        self.favorites = favorites
        self.users = users
        Club.all_clubs.append(self)
        Club.all_names.append(name)

    def increaseFavorites(self):
        self.favorites += 1

    #Gets the club info that needs to be posted on api/clubs - club names and number of favorites
    def clubInfo(self):
        all_info = []
        for club in Club.all_clubs:
            info = {
            'name' : club.name,
            'favorites' : club.favorites
        }
            all_info.append(info)
        return all_info

    #Adds new user emails that join a club
    def updateUser(self, user):
        self.users.append(user)


class User:
    #List of all users created
    all_users = []
    #List of all usernames created
    all_usernames = []
    #Intialize with a name, username, email, grad year, club names that they've favorited, a password, and clubs that they've joined
    def __init__(self, name, username, year, email, favorites, password, clubs):
        self.name = name
        self.username = username
        self.year = year
        self.favorites = favorites
        self.password = password
        self.clubs = clubs
        self.email = email
        User.all_users.append(self)
        User.all_usernames.append(self.username)

    #User info that gets put on their profile - excludes password
    def userInfo(self):
        user = {
            'name': self.name,
            'username': self.username,
            'year': self.year,
            'favorites': self.favorites,
            'clubs': self.clubs,
            'email': self.email
        }
        return user

    def updateFavorites(self, fav):
        self.favorites = self.favorites.append(fav)

    def updateClubs(self, club):
        self.clubs = self.clubs.append(club)

#Uses scraper to create all the club objects
def createClubs():
    soup = soupify(get_clubs_html())
    club_soups = get_clubs(soup)
    for x in range(len(club_soups)):
        Club(get_club_name(club_soups[x]), get_club_description(club_soups[x]), get_club_tags(club_soups[x]), 0, [])

#This code was used for testing purposes and to create Jennifer
createClubs()
user1 = User("Jennifer", "jen", 2022, "jen@seas.upenn.edu", [], "jenspass", ["Penn Labs", "Penn Program for Potential Procrastinators"])
print(user1.clubs)

club = Club.all_clubs[1]
club.updateUser("jen@seas.upenn.edu")
club2 = Club.all_clubs[2]
club2.updateUser("jen@seas.upenn.edu")
print(club2.users)
#


@app.route('/')
def main():
    return "Welcome to Penn Club Review!"

@app.route('/api')
def api():
    return "Welcome to the Penn Club Review API!."

@app.route('/api/clubs', methods = ['GET', 'POST'])
def get_clubs():
    if request.method == 'POST':
        count = 0
        #First checks if the club sent in the request exists and updates the club info
        for clubs in Club.all_clubs:
            if clubs.name == request.json['name']:
                count = 1
                club = clubs
                clubs.description = request.json['description']
                clubs.tags = request.json['tags']
        #If the club does not exist then we create a new club that is also added to existing club page
        if count == 0:
            club = Club(request.json['name'], request.json['description'], request.json['tags'], 0, []).__dict__
        return jsonify({'clubs': club})
    #If it's a GET request then we just show all the club names and the number of favorites for each
    else:
        club = Club.all_clubs[0]
        return jsonify({'clubs' : club.clubInfo()}) #shows all club names only
       # return jsonify({'clubs' : Club.all_clubs}) - if want all club info


@app.route('/api/user/<username>', methods = ['GET'])
def show_user_profile(username):
    for item in User.all_users:
        if item.username == username:
            user = item
            user_info = user.userInfo()

    return jsonify({'user' : user_info})


@app.route('/api/favorite', methods = ['POST'])
def update_favorites():
    user = request.json['user']
    club = request.json['club']
    user.updateFavorites(club)
    club.increaseFavorites()
    return jsonify({'clubs': club}), 201

#Allows a user to join a club if they want - this adds their email to the club users variable 
#(Note that I made joining a club for the purpose of allowing people who are interested to conatct you / for future could
#allow you to join the listserv, etc.)
@app.route('/api/joinClub', methods = ['POST'])
def update_clubs():
    user = request.json['user']
    club = request.json['club']
    user.updateClubs(club.name)
    club.updateUser(user.email)
    return jsonify({'clubs': club}), 201

#Allows users to get all the emails of members of a certain club so that they can contact indiviuals if they are interested
#The url includes the club name
@app.route('/api/members/<club>', methods = ['GET'])
def getMembers(club):
    members = []
    for item in Club.all_clubs:
        name = item.name.replace(' ', '')
        if name == club:
            members = item.users
            print(members)

    return jsonify({'members': members})

if __name__ == '__main__':
    app.run()


