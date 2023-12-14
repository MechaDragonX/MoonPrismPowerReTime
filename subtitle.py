from datetime import time

class Subtitle:
    start_time = time(0, 0, 0)
    end_time = time(0, 0, 0)
    text = ''

    def __init__(self, start_time: time, end_time: time, text: str):
        self.start_time = start_time
        self.end_time = end_time
        self.text = text

    def __str__(self):
        start_string = f'{self.start_time.isoformat()[:-7]},{self.start_time.isoformat()[9:12]}'
        end_string = f'{self.end_time.isoformat()[:-7]},{self.end_time.isoformat()[9:12]}'
        return f'{start_string} --> {end_string}\n{self.text}'
