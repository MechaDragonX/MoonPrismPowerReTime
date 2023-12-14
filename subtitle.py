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
        start_str_main = self.start_time.isoformat(timespec='microseconds')[:-7]
        start_str_ms = self.start_time.isoformat(timespec='microseconds')[9:12]
        end_str_main = self.end_time.isoformat(timespec='microseconds')[:-7]
        end_str_ms = self.end_time.isoformat(timespec='microseconds')[9:12]
        start_string = f'{start_str_main},{start_str_ms}'
        end_string = f'{end_str_main},{end_str_ms}'
        return f'{start_string} --> {end_string}\n{self.text}'
