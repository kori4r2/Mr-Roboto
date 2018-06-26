from plannerClasses import User, Event, Group, Voting
import sqlite3
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

def initDatabase():
def getUser(id):
def updateUser(user):
def getGroup(id):
def updateGroup(group):
def getVotings(groupId):
def updateVotings(voting):
def getEvents(userId):
def deleteEvent(event):
def updateEvent(event):
def addEvent(userId, event):
def updateDatabase():
def clearDatabase():
