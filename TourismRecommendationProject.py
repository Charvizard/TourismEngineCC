
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Eqypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = [[], [], [], [], []]

def get_destination_index(destination) : 
    destination_index = 0
    for index in range(len(destinations)) : 
        if destination == destinations[index] : 
            destination_index = index
            break
        else : 
           print("Destination not found yet")
    return destination_index; 

def get_traveler_location(traveler) : 
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

def add_attraction(destination, attraction) : 
    try :
        destination_index = get_destination_index(destination) 
    except ValueError : 
        print("THe destination was not found")
        return 
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)



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
print(attractions)
print(test_destination_index)