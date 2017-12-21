import functools

def convert_particle_string_to_coordinates(particle_string):
    coordinate_string = particle_string.split('<')[-1]
    return list(map(int, coordinate_string.split(',')))


def increment_properties():
    for particle in particles:
        for i in range(0, 3):
            particle['v'][i] += particle['a'][i]
        for i in range(0, 3):
            particle['p'][i] += particle['v'][i]


def is_location_match(position1, position2):
    return position1[0] == position2[0] and position2[0] == position1[0] and position1[2] == position2[2]


def get_matching_particles(particle_to_match):
    matching_particles = []
    position_to_match = particle_to_match['p']
    for particle in particles:
        if is_location_match(position_to_match, particle['p']) is True:
            matching_particles.append(particle)

    return matching_particles


def resolve_collisions():
    for particle in particles:
        matching_particles = get_matching_particles(particle)

        if len(matching_particles) > 1:
            print("Found particles to remove", len(matching_particles))
            for mp in matching_particles:
                print("removing", mp['p'], mp['i'])
                particles.remove(mp)



def compute_particle_distance(position):
    return functools.reduce(lambda x, y: x+y, map(abs, position))


def find_particle_with_shortest_difference():
    min_distance = 1000000000000000
    min_distance_particle = -1

    for i, particle in enumerate(particles):
        distance = 0
        for property in ('p', 'v', 'a'):
            distance += compute_particle_distance(particle[property])

        if distance < min_distance:
            min_distance = distance
            min_distance_particle = (i, particle)

    return min_distance, min_distance_particle


with open('Input.txt', 'r') as f:
    initial_state = f.readlines()


particles = []

for state in initial_state:
    tokens = state.split('>')

    particle = {}
    for index_identifier in ("0:p", "1:v", "2:a"):
        index = int(index_identifier[0])
        identifier = index_identifier[2]
        particle[identifier] = convert_particle_string_to_coordinates(tokens[index])

    particle["i"] = len(particles)
    particles.append(particle)

counter = 0

print(particles)

while True:
    resolve_collisions()
    increment_properties()
    #print(find_particle_with_shortest_difference())
    print(len(particles))