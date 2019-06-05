"""
Former Google code challenge
https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#code-challenge
"""
import re
import sys


class Decompresser:

    def __init__(self):
        self.regex = re.compile(r'\d+\[\w+\]')

    def decompress(self, string):
        mob = re.search(self.regex, string)
        while mob is not None:
            substr, idxs = mob[0], mob.span()
            split = substr.split('[')
            dup, substr = int(split[0]), split[1][:-1]
            string = string[:idxs[0]] + dup * substr + string[idxs[1]:]
            mob = re.search(self.regex, string)
        return string


if __name__ == "__main__":
    dec = Decompresser()
    string = sys.argv[1]
    print(string)
    string = dec.decompress(string)
    print(string)
