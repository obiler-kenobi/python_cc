#original order
places_to_visit = ['japan','england','switzerland','usa','singapore']
print(places_to_visit)

#temporarily sorting the list
print(sorted(places_to_visit))
print(places_to_visit)

#using sorted(reverse=True) to print the list in reverse order
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)

#reversing the list
places_to_visit.reverse()
print(places_to_visit)

#changing the reverse list back to its original order
places_to_visit.reverse()
print(places_to_visit)

#sorting the list to alphabetical order
places_to_visit.sort()
print(places_to_visit)

#sorting the list in reverse alphabetical order
places_to_visit.sort(reverse=True)
print(places_to_visit)
