# import special libraries already built in python
import random, urllib2

# list of options to select from
the_url = 'https://raw.githubusercontent.com/bellcodo/congenial-octo-meme/master/activities.lst'
list_raw_text = urllib2.urlopen(the_url).read()

# print "DEBUG: " + str(list_raw_text.split())

possible_activities = list_raw_text.split()

# choice of what we are going to do
the_activity = random.choice(possible_activities)

# display the results to the end user
print "Possible activities are: " + str(possible_activities)
print "What we are going to do: " + the_activity
