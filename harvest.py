############
# Part 1   #
############

"""Create a list of dictionarys for melon data to run through Make_Melon_Types function. """
melons = [{
    'code': 'musk',
    'first_harvest': 1998,
    'color': 'green',
    'is_seedless': True,
    'is_bestseller': True,
    'pairs_with': ['mint'],
    'name': 'Muskmelon'
},
{
    'code': 'cas',
    'first_harvest': 2003,
    'color': 'orange',
    'is_seedless': False,
    'is_bestseller': False,
    'pairs_with': ['strawberries', 'mint'],
    'name': 'Casaba'   
},
{
    'code': 'cren',
    'first_harvest': 1996,
    'color': 'green',
    'is_seedless': False,
    'is_bestseller': False,
    'pairs_with': ['proscuitto'],
    'name': 'Crenshaw'
},
{
    'code': 'yw',
    'first_harvest': 2013,
    'color': 'yellow',
    'is_seedless': False,
    'is_bestseller': True,
    'pairs_with': ['ice cream'],
    'name': 'Yellow Watermelon'
}
]

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name):
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    """Initialize a melon."""
        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        self.pairings.append(pairing)
       

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
       
        self.code = new_code
        


def make_melon_types(melons):
    """Returns a list of current melon types."""

    all_melon_types = []

    for melon in melons:
        #set each melon dictionary key value equal to a var to call in MelonType class call
        key_code = melon['code']
        key_first_harvest = melon['first_harvest']
        key_color = melon['color']
        key_is_seedless = melon['is_seedless']
        key_is_bestseller = melon['is_bestseller']
        key_name = melon['name']
        key_pairs = melon["pairs_with"]
        

        new_melon = MelonType(key_code, key_first_harvest, key_color, key_is_seedless, key_is_bestseller, key_name)
        for pair in key_pairs:
            new_melon.add_pairing(pair)
        all_melon_types.append(new_melon)


    return all_melon_types

test_melons_list = make_melon_types(melons)


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # Input - list of melon type instances of MelonType class
    # Output - printing strings with Melon name and what it pairs with
    for melon in melon_types:
            melon_type = melon.name
            melon_pairs = melon.pairings
            
            print(f"{melon_type} pairs with:")
            for pair in melon_pairs:
                print(f"- {pair}")
        
            

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



