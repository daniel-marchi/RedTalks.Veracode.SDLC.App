# models.py defines database tables that get created, in addition to blabbers class
import hashlib
import moment

from django.db import models


# User model stores user information
class User(models.Model):
    
    class Meta:
        db_table='users'
    
    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100,null=True)
    password_hint = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(null=True)
    last_login = models.DateTimeField(null=True)
    real_name = models.CharField(max_length=100, null=True)
    blab_name = models.CharField(max_length=100, null=True)

# Creates a new user from just username, blabname, and realname
def create(userName, blabName,realName):
    password = userName
    dateCreated = moment.now().format("YYYY-MM-DD hh:mm:ss")
    lastLogin = None
    return User(userName, hashlib.md5(password.encode('utf-8')).hexdigest(), userName, dateCreated, lastLogin, blabName, realName)

# Table for a blab, which is a message on the website
class Blab(models.Model):
    class Meta:
        db_table='blabs'

    date_format = "%b %d %Y"

    blabid = models.IntegerField('''max_length=11''',null=False,primary_key=True)
    blabber = models.TextField(max_length=100,null=False)
    timestamp = models.DateTimeField(null=True)
    content = models.TextField(max_length=250, null=True)
    commentCount = 0
    author = None
    
    ######Getters and setters######
    def getId(self):
        return self.blabid

    def setId(self, blabid):
        self.blabid = blabid

    def getContent(self):
        return self.content

    def setContent(self, content):
        self.content = content

    def getPostDate(self):
        return self.timestamp
    
    def getPostDateString(self):
        return self.timestamp.strftime(self.date_format)

    def setPostDate(self, timestamp):
        self.timestamp = timestamp

    def getAuthor(self):
        return self.author
    
    def setAuthor(self, author):
        self.author = author

    def getCommentCount(self):
        return self.commentCount

    def setCommentCount(self, count):
        self.commentCount = count

# Blabber object, similar to a user but not needed in database    
class Blabber():

    id = None
    username = None
    realName = None
    blabName = None
    createdDate = None
    numberListeners = None
    numberListening = None

    date_format = "%b %d %Y"
    ######Getters and Setters######
    def getId(self):
        return self.id
    
    def setId(self, newID):
        self.id = newID
    
    def getUsername(self):
        return self.username
        
    def setUsername(self, username):
        self.username = username

    def getRealname(self):
        return self.realName
    
    def setRealName(self, realName):
        self.realName = realName

    def getBlabName(self):
        return self.blabName
    
    def setBlabName(self, blabName):
        self.blabName = blabName

    def getCreatedDate(self):
        return self.createdDate
    
    def getCreatedDateString(self):
        return self.createdDate.strftime(self.date_format)

    def setCreatedDate(self, createdDate):
        self.createdDate = createdDate

    def getNumberListeners(self):
        return self.numberListeners
    
    def setNumberListeners(self, numberListeners):
        self.numberListeners = numberListeners

    def getNumberListening(self):
        return self.numberListening
    
    def setNumberListening(self, numberListening):
        self.numberListening = numberListening

# Table layout for a comment
class Comment(models.Model):

    commentid = models.IntegerField(primary_key=True,null=False)
    blabid = models.IntegerField(null=False)
    blabber = models.TextField(max_length=100, null=False)
    content = models.TextField(max_length=250, null=True)
    timestamp = models.DateTimeField(null=True)

    date_format = "%b %d %Y"

    # Renames the table in database
    class Meta:
        db_table = 'comments'

    ######Getters and setters######
    def getId(self):
        return self.commentid

    def setId(self, commentid):
        self.commentid = commentid

    def getContent(self):
        return self.content

    def setContent(self, content):
        self.content = content

    def getTimestamp(self):
        return self.timestamp
    
    def getTimestampString(self):
        return self.timestamp.strftime(self.date_format)

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def getAuthor(self):
        return self.blabber
    
    def setAuthor(self, blabber):
        self.blabber = blabber

# Table of Listeners
class Listener(models.Model):
    blabber = models.TextField(max_length=100,null=False)
    listener = models.TextField(max_length=100,null=False)
    status = models.TextField(max_length=20,null=True)
    #Renames table
    class Meta:
        db_table = 'listeners'

# Creates table of user history
class User_History(models.Model):
    #Renames table
    class Meta:
        db_table = 'users_history'

    eventid = models.IntegerField(primary_key=True)
    blabber = models.TextField(max_length=100)
    event = models.TextField(max_length=250,null=True)
    timestamp = models.DateTimeField(null=True)

