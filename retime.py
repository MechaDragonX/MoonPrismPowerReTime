from datetime import time
import re
from subtitle import Subtitle

def read_file(path: str) -> list:
    lines = []
    with open(path, 'r') as file:
        lines = file.readlines()
    
    lines[0] = '1'

    i = 1
    while i < len(lines):
        lines[i] = lines[i][:-1]
        i += 1
    
    return lines


def import_subtitles(file_text: list) -> list:
    # importing = False
    start_time_pattern = re.compile('.+?(?= --> )')
    end_time_pattern = re.compile('(?<= --> )[^\]]+')
    start_time = time(0, 0, 0)
    end_time = time(0, 0, 0)
    text_array = []
    text = ''
    i = 0
    current = None
    subtitles = []

    for line in file_text:
        if line.isdigit():
            # importing = True
            start_time = time(0, 0, 0)
            end_time = time(0, 0 , 0)
            text_array.clear()
            text = ''
            current = None

        elif line == '':
            i = 0
            while i < len(text_array):
                if i == len(text_array) - 1:
                    text += text_array[i]
                else:
                    text += f'{text_array[i]}\n'
                i += 1
            current = Subtitle(start_time, end_time, text)
            subtitles.append(current)
            # importing = False

        elif (len(line) == 29) and (' --> ' in line):
            start_time = time.fromisoformat(
                re.search(start_time_pattern, line).group()
            )
            end_time = time.fromisoformat(
                re.search(end_time_pattern, line).group()
            )

        else:
            text_array.append(line)
    
    return subtitles


def write_to_srt(subtitles: list, path: str) -> None:
    content = []
    i = 0
    while i < len(subtitles):
        content.append(f'{str(i + 1)}\n')
        content.append(f'{str(subtitles[i])}\n')
        content.append('\n')
        i += 1

    with open(path, 'w') as file:
        file.writelines(content)


def recreate(input_path: str, output_path: str):
    lines = read_file(input_path)
    subtitles = import_subtitles(lines)
    write_to_srt(subtitles, output_path)


recreate('test.srt', 'out.srt')
