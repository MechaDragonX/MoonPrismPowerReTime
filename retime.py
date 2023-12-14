from datetime import time
import re
from subtitle import Subtitle

test = [
    '1',
    '00:00:02,430 --> 00:00:05,420',
    'エリマキトカゲや',
    'ウーパールーパーや',
    ''
]

# importing = False
start_time_pattern = re.compile('.+?(?= --> )')
end_time_pattern = re.compile('(?<= --> )[^\]]+')
start_time = time(0, 0, 0)
end_time = time(0, 0, 0)
text_array = []
text = ''
current = None

for line in test:
    if line.isdigit():
        # importing = True
        start_time = time(0, 0, 0)
        end_time = time(0, 0 , 0)
        text_array.clear()
        text = ''

    elif line == '':
        i = 0
        while i < len(text_array):
            if i == len(text_array) - 1:
                text += text_array[i]
            else:
                text += f'{text_array[i]}\n'
            i += 1
        current = Subtitle(start_time, end_time, text)
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

print(current)
