class Datamanager:
    def __init__(self, data):
        self.data = data
        self.speed = np.zeros(data.size)
        self.acceleration = np.zeros(data.size)
    def give_data(self):
        return self.data
    def calculate(self, c_speed):
        self.data += self.speed
        self.speed += self.acceleration
        self.acceleration = acceleration_operator(self.data, c_speed)
