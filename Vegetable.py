#код Манжесова Алексея
class Vegetable():
    def __init__(self, name, water, nutrients, light):
        self.name = name
        self.water = water 
        self.nutrients = nutrients
        self.light = light

    def __repr__(self):
        return f'''
Вид образца: {self.name}
Обеспеченность водой: {self.water:.2f}
Обеспеченность питательными веществами: {self.nutrients:.2f}
Обеспеченность светом: {self.light:.2f}'''

    def check_state(self, required_water, required_nutrients, required_light):
        if (self.water >= required_water and self.nutrients >= required_nutrients and self.light >= required_light):
            print('Результат: образец выжил')
            return True
        else:
            print('Результат: образец погиб')  
            return False  
