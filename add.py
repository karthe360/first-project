class car:
    def __init__(self,car_rank,car_name,car_id):
        self.car_rank=car_rank
        self.car_name=car_name
        self.car_id=car_id
    def car_bio(self):

        print("The ranking of car :",self.car_rank,self.car_name,self.car_id)


hifi_cars1=car("FIRST","JAGUAR",9999)
hifi_cars2=car("SECOND","FERRARI",3535)
hifi_cars3=car("THIRD","BMW",3333)
print("###..welcome to car mania..###")
hifi_cars1.car_bio()
hifi_cars2.car_bio()
hifi_cars3.car_bio()
