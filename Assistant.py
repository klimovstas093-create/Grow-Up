class Assistant():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def print_info(self):
        print('Лаборант:', self.name, 'Должность:', self.position)

    def water_sample(self, sample): 
        sample.water += 1
        print(self.name,'полил образец, обеспеченность водой образца:', sample.water)

    def udobrenie_sample(self, sample):
        sample.nutrient += 1
        print(self.name, 'внес удобрение на образец, обеспеченность питательными веществами образца:', sample.nutrient)

    def light_sample(self, sample):
        sample.light += 1
        print(self.name, 'включил дополнительное освещение для образца, обеспеченность светом образца:',  sample.light)

    def check_certificate(self, sample):
        if sample.water > 0 and sample.nutrient > 0 and sample.light > 0:
            print('Прошёл аттестацию и допущен до работы с настоящими опытными образцами.')
        elif sample.water <= 0 and sample.nutrient <= 0 and sample.light <= 0:
            print('Не прошёл аттестацию. Отправляется на пересдачу.')
