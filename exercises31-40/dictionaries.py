#dictionary of state names to abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'Michigan': 'MI'
}

#dictionary of a major city in a given state
cities = {
    'CA': 'San Francisco',
    'MI': 'Detriot',
    'FL': 'Jacksonville'
}

#let's add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" %(state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])
    
#how to safely get an abbreviation that might not be there
print '-' * 10
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas"

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" %city