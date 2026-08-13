#код Бабошина Максима
class Assistant():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __repr__(self):
        return 'Лаборант:', self.name, 'Должность:', self.position

    def water_sample(self, sample): 
        sample.water += 1
        print(self.name,'полил образец, обеспеченность водой образца:', sample.water)

    def udobrenie_sample(self, sample):
        sample.nutrients += 1
        print(self.name, 'внес удобрение на образец, обеспеченность питательными веществами образца:', sample.nutrients)

    def light_sample(self, sample):
        sample.light += 1
        print(self.name, 'включил дополнительное освещение для образца, обеспеченность светом образца:',  sample.light)

    def check_certificate(self, samples_states):
        if False in samples_states:
            print(self.name, 'не прошёл аттестацию. Отправляется на пересдачу.')
        else:
            print(self.name, 'прошёл аттестацию и допущен до работы с настоящими опытными образцами.')
