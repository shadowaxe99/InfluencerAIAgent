
import datetime
import os

from pymongo import MongoClient

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
db = client[os.getenv('MONGODB_DB', 'influencer_platform')]
collection = db[os.getenv('MONGODB_COLLECTION', 'contactDatabase')]

# Shared variables
contactDatabase = []
appointmentSchedule = []

def manageContacts():
    global contactDatabase
    contacts = collection.find()
    for contact in contacts:
        contactDatabase.append(contact)

def scheduleAppointments():
    global appointmentSchedule
    for contact in contactDatabase:
        if 'next_appointment' in contact:
            if contact['next_appointment'] < datetime.datetime.now():
                contact['next_appointment'] = datetime.datetime.now() + datetime.timedelta(days=7)
                appointmentSchedule.append(contact)

manageContacts()
scheduleAppointments()
```