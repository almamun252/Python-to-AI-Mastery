class Robot:
    # Class Variable
    laws_of_robotics = 3

    def __init__(self, name, model):
        # Instance Variables
        self.name = name
        self.model = model

    # Method
    def introduce(self):
        print(f"Hello, I am {self.name}, model {self.model}.")

# Objects creation
robot1 = Robot("Optimus", "T-800")
robot2 = Robot("Wall-E", "Trash-Compactor")


print(f"Robot laws: {Robot.laws_of_robotics}")
robot1.introduce()
robot2.introduce()