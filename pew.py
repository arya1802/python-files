class Car:
    def __init__(self,model,color):
        self.color=color
        self.model=model
    def start(self):
        print("ready to rage")

audi=Car("q5","blue")
audi.start()

