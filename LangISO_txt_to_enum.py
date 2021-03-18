
with open('Website/Tweets/ISO639Lang.py', 'w', encoding='utf-8') as writer:
    writer.write('from enum import Enum\n\n')
    writer.write('\nclass LangISO(Enum):\n\n')
    with open('ISO639Lang.txt', 'r', encoding='windows-1252') as reader:
        lines = reader.readlines()
        for line in lines:
            line = line.split('|')
            line3 = line[3].split('; ')
            line[3] = ''
            for name in line3:
                if line3.index(name) != len(line3) - 1:
                    line[3] += f'{name},'
                else:
                    line[3] += f'{name}'
            if line[2] != '':
                writer.write(f'    var_{line[2]} = ("{line[2]}", "{line[3]}")\n')
