"""
This module contains the WelcomeEmail class, which is used to create
and send welcome emails.
"""


class WelcomeEmail:
    """Class used to create a welcome email"""

    def __init__(self):
        """Initializes the list of people"""
        self.people = ["Wallace", "Mazoelle", "Fabricio", "Fabio", "Sidney"]

    def start(self):
        """Starts the process of creating and sending welcome credentials"""
        print("hello")
        welcome_emails = self.create_credentials(self.people)
        for email in welcome_emails:
            print(email)

    def create_credentials(self, people):
        """Creates welcome messages for each person in the list"""
        credentials = []
        for person in people:
            message = f"The company welcomes you {person}"
            credentials.append(message)
        return credentials


# Creates an instance of the WelcomeEmail class and calls the start method
welcome_email = WelcomeEmail()
welcome_email.start()
