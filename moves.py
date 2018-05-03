class Move:
    better_than = None
    worse_than = None

    def __gt__(self, other):
        """Is this instance being compared to an instance from a worse class"""
        return other.__class__.__name__ in self.better_than

    def __lt__(self, other):
        """Is this instance being compared to an instance from a better class"""
        return other.__class__.__name__ in self.worse_than

    def __eq__(self, other):
        """Is this instance being compared to an instance from the same class"""
        return type(other) == type(self)

    def __ne__(self, other):
        """Is this instance being compared to an instance from another class"""
        return other.__class__ != self.__class__


class Rock(Move):
    better_than = ['Scissors', 'Lizard']
    worse_than = ['Paper', 'Spock']


class Paper(Move):
    better_than = ['Rock', 'Spock']
    worse_than = ['Scissors', 'Lizard']


class Scissors(Move):
    better_than = ['Paper', 'Lizard']
    worse_than = ['Rock', 'Spock']

class Lizard(Move):
    better_than = ['Spock', 'Paper']
    worse_than = ['Scissors', 'Rock']

class Spock(Move):
    better_than = ['Rock', 'Scissors']
    worse_than = ['Lizard', 'Paper']
