import datetime


class Scheduler:
    def __init__(self, schedule, reminders):
        self.schedule = schedule
        self.reminders = reminders

    def add_reminder(self, reminder):
        self.reminders.append(reminder)

    def send_reminder(self, reminder):
        print(f"Reminder sent: {reminder}")

    def update_schedule(self, new_schedule):
        self.schedule = new_schedule
