
class Timer:
    def __init__(self, time):
        self.time = time

    def __str__(self):
        sec = self.time

        hour = sec // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60

        H = str(hour).zfill(2)
        M = str(min).zfill(2)
        S = str(sec).zfill(2)

        return H + ':' + M + ':' + S

    def update(self):
        self.time -= 1

'''
def time_format(sec):
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60

    H = str(hour).zfill(2)
    M = str(min).zfill(2)
    S = str(sec).zfill(2)

    return H + ':' + M + ':' + S

print(time_format(125))
'''


t = Timer(125)
print(t)
