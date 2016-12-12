import collections
import itertools
import functools

"""

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

"""


def parse_input(input_string):
    for line in input_string.splitlines():
        name_and_sector, checksum = line[:-1].split("[")
        name_and_sector = name_and_sector.split("-")
        name = tuple(name_and_sector[:-1])
        sector = int(name_and_sector[-1])
        yield name, sector, checksum


def _cmp_elements(e1, e2):
    e1_l, e1_c = e1
    e2_l, e2_c = e2
    if e1_c < e2_c:
        return 1
    if e1_c > e2_c:
        return -1
    if e1_l < e2_l:
        return -1
    if e1_l > e2_l:
        return 1
    return 0


def check_checksum(name, checksum):
    counter = collections.Counter("".join(name))
    els = list(
        sorted(counter.most_common(),
               key=functools.cmp_to_key(_cmp_elements)))[:5]
    return checksum == "".join([l for (l, c) in els])


def sum_valid_sectors(seq):
    result = 0
    for name, sector, checksum in seq:
        if check_checksum(name, checksum):
            result += sector
    return result


def decrypt(name, shift):
    base = ord("a")
    decrypted = [[chr(base + ((ord(x) - base + shift) % 26)) for x in item]
                 for item in name]
    return " ".join("".join(x) for x in decrypted)


def find_north_pole(seq):
    for name, sector, checksum in seq:
        if check_checksum(name, checksum):
            print(decrypt(name, sector))
            if decrypt(name, sector).startswith("north"):
                return sector


if __name__ == '__main__':
    with open("data/4.txt") as inp:
        inp_str = inp.read()
        parsed_input = list(parse_input(inp_str))
        print(sum_valid_sectors(parsed_input))
        print(find_north_pole(parsed_input))
