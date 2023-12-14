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
        return f'Start Time: {self.start_time}\nEnd Time: {self.end_time}\n{self.text}'
