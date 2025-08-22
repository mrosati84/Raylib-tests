from simulation import Simulation
from entities.ship import Ship
from entities.station import Station
from generic_task import Task

if __name__ == "__main__":
    simulation = Simulation()

    t1 = Task("MOVE", destination=(0, 0))
    t2 = Task("LOAD", cargo=10)

    ship = Ship(1, pos=(7, 12), cargo=0, tasks=[t1, t2])
    station = Station(2, pos=(0, 0), cargo=10, tasks=[])

    simulation.add_agent(ship)
    simulation.add_agent(station)

    try:
        while True:
            simulation.tick()
            input("")
    except KeyboardInterrupt:
        print("\nQuitting...")
