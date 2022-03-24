import pygame
import math
pygame.init()

#setting window for simulator
WIDTH, HEIGHT = 650, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#set title of window
pygame.display.set_caption("Planet simulator")

WHITE = (255,255,255)
YELLOW = (255,255,0)
BLUE = (100,149,237)
RED = (188,39,50)
DARK_GREY = (80,78,81)
FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
    #constants used for simulation
    AU = 149.6e6 * 1000 #astronomical units, approx distance of earth to sun, set in metres
    GC = 6.67428e-11 #gravitational constant
    SCALE = 175/AU #reduced scale for pixels on pygame window, 1AU = 100pixels
    TIMESTEP = 3600*24 #everytime a frame is used, how much time is passed, 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = [] # used to keep track of places planet has travelled to
        self.sun = False #setting whether it is sun
        self.distance_to_sun = 0

        #velocities
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2


        if len(self.orbit) > 2:
            #all x and y coordinates stored in updated points
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH/2
                y = y * self.SCALE + HEIGHT/2
                updated_points.append((x,y))

            #draw lines from updated points in order to have orbit lines, 2 is thickness of line
            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x,y), self.radius)

        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)} km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width()/2, y  -distance_text.get_width()/2))

    def attraction(self, other):
        #other is the other planet in relation to current planet
        other_x, other_y = other.x, other.y
        #calc distance between current planet and other planet
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        #if other object is the sun
        if other.sun:
            self.distance_to_sun = distance

        force = self.GC * self.mass * other.mass / distance**2 #gravitational force between 2 objects
        theta = math.atan2(distance_y, distance_x) #angle theta used to calc x-force and y-force
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_force_x = total_force_y = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_force_x += fx
            total_force_y += fy

        #calculate velocity of planet based on total force x and y
        self.x_vel += total_force_x / self.mass * self.TIMESTEP #f=ma
        self.y_vel += total_force_y / self.mass * self.TIMESTEP

        #update x and y position by using the calculated velocities
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

def main():
    run = True
    #set framerate and refresh rate
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892*10**30)
    sun.sun = True


    #planets, planet y velocity needs to be provided or planets will just move straight towards sun
    mercury = Planet(-0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30*10**23)
    mercury.y_vel = 47.4 * 1000
    venus = Planet(-0.723 * Planet.AU, 0, 14, WHITE, 4.8685*10**24)
    venus.y_vel = 35.02 * 1000
    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742*10**24)
    earth.y_vel = 29.783 * 1000
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39*10**23)
    mars.y_vel = 24.077 * 1000

    planets = [sun, mercury, venus, earth, mars]

    #keep looping, if user clicks on close button for pygame window, loop stops run and close
    while run:
        clock.tick(60) #max of 60fps
        WIN.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()

main()