import json
import fileinput
import sys
import itertools
import re

def output(stem, meaning, examples, origin):
    output_dict = {'question': 'Stem: {}\nExamples: {}\nOrigin: {}\n'.format(stem, examples, origin),
                   'answer': meaning}
    return output_dict

if __name__ == '__main__':
    output_array = []
    with open(sys.argv[1]) as f:
        while True:
            first_line = f.readline()
            if first_line == '':
                break
            first_line = first_line.strip()
            vocab_item = re.sub(r'([0-9]+\.)?\s*', '', first_line)
            question = ''
            first = True
            while True:
                last_pos = f.tell()
                line = f.readline().strip()
                match = re.match(r'[a-z]\.', line)
                if match or first:
                    question += line + '\n'
                if not match and first:
                    break
                if not match:
                    f.seek(last_pos)
                    break
                first = False
            output_array.append({'question': question,
                                 'answer': vocab_item})

    print json.dumps(output_array, indent=4)
