#ДЗ 33. Цифровой счётчик

class digitalСounter:

    def v_work(self):
        self.work += 1
        self.v_now = self.work
        return self.work

    def __init__(self, v_min=0, v_max=0, v_now=0):
        self.work = v_now
        self.v_min = v_min
        self.v_max = v_max


count = digitalСounter(0, 100, 10) 

# Проверка работы
print(count.v_work())
print(count.v_work())
print(count.v_now)
print(count.v_now)
print(count.v_work())
print(count.v_work())
print(count.v_min)
print(count.v_max)
