destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Eqypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = [[], [], [], [], []]

def get_destination_index(destination) : 
    destination_index = 0
    for index in range(len(destinations)) : 
        if destination == destinations[index] : 
            destination_index = index
    return destination_index; 

def get_traveler_location(traveler) : 
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

def add_attraction(destination, attraction) : 
    try :
        destination_index = get_destination_index(destination) 
    except ValueError : 
        print("The destination was not found")
        return 
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)

def find_attractions(destination, interests) : 
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city : 
        possible_attraction = attraction
        attraction_tags = attraction[1]
        for interest in interests : 
            for tag in range(len(attraction_tags)) :  
                if interest == attraction_tags[tag] :
                    attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

def get_attractions_for_traveler(traveler) : 
    traveler_destination = traveler[1]
    traveler_interest = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interest)
    interests_string = "Hi, " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
    for attraction in traveler_attractions : 
        interests_string += attraction + ", "
    return interests_string

test_destination_index = get_traveler_location(test_traveler)
add_attraction("Los Angeles, USA",['Venice Beach', ['beach']] )
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(test_destination_index)
la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)