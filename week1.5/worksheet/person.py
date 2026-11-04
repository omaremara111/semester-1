# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def __init__(self, name, birth):
        """
        Create a person with a name and a date of birth.
        """
        self.name = name
        self.birth = birth

        if not isinstance(self.name, str):
            raise TypeError("Name must be a string")

        if name == "":
            raise ValueError("Name cannot be empty")
        
        if not isinstance(self.birth, date):
            raise TypeError("Birth must be a date object")

    def initials(self):
        """
        Returns the intials of the persons name as a string in Uppercase.
        """
        return"".join(name[0].upper() for name in self.name.split())

    def is_birthday(self):
        """
        Returns True if today is the person's birthday, False otherwise.
        """
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day
        
    

    
