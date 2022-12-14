from __future__ import annotations
import sys
from itertools import zip_longest
from typing import Iterable

# Parse the music notes in https://pianoletternotes.blogspot.com/2018/03/bad-apple-teppei-okada.html
# and convert them to frequencies using https://www.liutaiomottola.com/formulae/freqtab.htm
# Then output `beep` commands to the input file

music_notes = """\
4|D--D-D--DC-dD--D-D--DC-dD-|
4|-D-D--DC-dD--D-FG--F-GD--D|
4|-D--DC-dD--D-D--DC-dD--D-D|
4|--DC-dG--F-GF--D-FD--D-D--|
4|DC-dD--D-D--DC-dD--D-D--DC|
4|-dD--D-FG--F-GD--D-D--DC-d|
4|D--D-D--DC-dD--D-D--DC-dG-|
4|F-G-F-D-F-D--f--F--G--A---|
5|--D--C--------------------|
4|--------A-----D-----A--G--|
4|F--f--D--f--F--G--A-----G-|
4|-F--f--D--f--F--f--D--d--f|
5|--------------------D--C--|
4|--D--f--F--G--A-----------|
4|A-----D-----A--G--F--f--D-|
4|-f--F--G--A-----G--F--f---|
4|--F-----G-----A-----D--f--|
5|------------D--C----------|
4|D--f--D-----F--A--F-----D-|
4|F--G--A-----------A-------|
3|------------------------A-|
4|----F--G--F--f--D--f--F--G|
4|----A---------------------|
4|--A-----G--F--f--D--f--F--|
4|f--D--d--f--D--f--D--f--D-|
4|------------------F--G--A-|
5|----D--C------------------|
4|----F--A--F-----D-----F--G|
4|----------A-----------A---|
3|----------------A---------|
4|--F--f--D--f--F--G--A-----|
4|G--F--f-----F-----G-----A-|
5|----C--D------------------|
4|----------A--G--A-----G--A|
5|--C--D--------------------|
4|--------A--G--A-----G--A--|
4|G--F--f--C--D-----C--D--f-|
5|-------------------C--C--D|
4|-F--G--A--D-----A---------|
5|--------------------C--D--|
4|--A--G--A-----G--A--------|
4|A--G--A-----G--A--G--F--f-|
4|-C--D-----C--D--f--F--G--A|
5|-----------C--C--D--------|
4|--D-----A-----------A--G--|
5|------------C--D----------|
4|A-----G--A--------A--G--A-|
4|----G--A--G--F--f--C--D---|
4|--C--D--f--F--G--A--D-----|
5|---C--C--D----------------|
4|A-----------A--G--A-----G-|
5|----C--D--------------D--f|
4|-A--------A--G--A---------|
5|--F--f--D--C--------------|
4|--------------A-----G--A--|
6|---------------------C--C-|
5|------------------A-------|
4|G--F--f--C--D-------------|
6|-D--------------------C--D|
5|----A--G--A-----G--A------|
5|--A--G--A-----G--A--G--F--|
5|f--C--D-----C--D--f--F--G-|
6|-------------C--C--D------|
5|-A--D-----A-----------A--G|
6|--------------C--D--------|
5|--A-----G--A--------A--G--|
5|A-----G--A--G--F--f--C--D-|
5|----C--D--f--F--G--A--D---|
6|-----C--C--D--------------|
5|--A-----------A--G--A-----|
6|------C--D----------------|
5|G--A--------A--G--A-----G-|
5|-A--G--F--f--C--D-----C--D|
6|-----------------------C--|
5|--f--F--G--A--D-----A-----|
6|C--D--------------------C-|
5|------A--G--A-----G--A----|
6|-D--------------D--f--F--f|
5|----A--G--A---------------|
6|--D--C--------------------|
5|--------A-----G--A--G--F--|
5|f--C--D-------------------|
4|------------------D--D-D--|
4|DC-dD--D-D--DC-dD--D-D--DC|
4|-dD--D-FG--F-GD--D-D--DC-d|
4|D--D-D--DC-dD--D-D--DC-dG-|
4|-F-GF--D-FD--D-D--DC-dD--D|
4|-D--DC-dD--D-D--DC-dD--D-F|
4|G--F-GD--D-D--DC-dD--D-D--|
5|--------------------C-D-F-|
4|DC-dD--D-D--DC-dG-A-------|
5|A-G-----------------A-GF--|
5|G-Ff--F-fD--f-DC--D-------|
4|------------------------A-|
5|----C---------------------|
4|-------A--G--a--G-----F---|
6|--------------------C-----|
5|--------C--D--F--A--------|
4|--G--A--------------------|
6|---D-----D-----F--------f-|
5|A-------------------------|
6|-f--f--F--f--D--C--D------|
5|---------------------AA---|
6|-C-----------------C------|
5|-------G--A--G--A--------A|
5|GG-A--G--F--------FfDf--bA|
4|------------fDCD----------|
6|----DC-C------------------|
5|GA----b---bAGA--FfDf------|
4|----------------------FfDf|
5|-----------C-C---------C-C|
4|--DC-C--A-A---b-bA-Ab-b---|
3|----b---------------------|
5|D-Df--G-----F--------f----|
5|-G-----F--f--G--F--f--G--F|
5|--f-G-F-f-G-F-f-G-F-f-G-F-|
6|-------C----D-----f-----F-|
5|A-----A-------------------|
6|-f--f-----D-----C-----C-dD|
6|--------------------C--D--|
5|--A--G--A-----G--A--------|
5|A--G--A-----G--A--G--F--f-|
5|-C--D-----C--D--f--F--G--A|
6|-----------C--C--D--------|
5|--D-----A-----------A--G--|
6|------------C--D----------|
5|A-----G--A--------A--G--A-|
5|----G--A--G--F--f--C--D---|
5|--C--D--f--F--G--A--D-----|
6|---C--C--D----------------|
5|A-----------A--G--A-----G-|
6|----C--D------------------|
5|-A--------A--G--A-----G--A|
5|--G--F--f--C--D-----C--D--|
6|---------------------C--C-|
5|f--F--G--A--D-----A-------|
6|-D--------------------C--D|
5|----A--G--A-----G--A------|
6|--------------D--f--F--f--|
5|--A--G--A-----------------|
6|D--C----------------------|
5|------A-----G--A--G--F--f-|
6|-------------d--d--e------|
5|-C--D-----b-----------b--a|
6|--------------d--e--------|
5|--b-----a--b--------b--a--|
5|b-----a--b--a--g--F--d--e-|
5|----d--e--F--g--a--b--e---|
6|-----d--d--e--------------|
5|--b-----------b--a--b-----|
6|------d--e----------------|
5|a--b--------b--a--b-----a-|
5|-b--a--g--F--d--e-----d--e|
6|-----------------------d--|
5|--F--g--a--b--e-----b-----|
6|d--e--------------------d-|
5|------b--a--b-----a--b----|
6|-e------------------------|
5|----b--a--b-----a--b--a--g|
5|--F--d--e-----d--e--F--g--|
6|---------------d--d--e----|
5|a--b--e-----b-----------b-|
6|----------------d--e------|
5|-a--b-----a--b--------b--a|
6|--------e--F--g--F--e--d--|
5|--b-----------------------|
5|b-----a--b--a--g--F--d--e-|"""


conversion_table = {
    0: {
        "a": 27.5,
        "b": 30.868,
        "c": 32.703,
        "d": 18.354,
        "e": 20.601,
        "f": 21.827,
        "g": 24.499,
        "A": 29.135,
        # 'B': 0,
        "C": 17.324,
        "D": 19.445,
        # 'E': 0,
        "F": 23.124,
        "G": 25.956,
    },
    1: {
        "a": 55,
        "b": 61.735,
        "c": 32.703,
        "d": 36.708,
        "e": 41.203,
        "f": 43.654,
        "g": 48.999,
        "A": 58.27,
        # 'B': 0,
        "C": 34.648,
        "D": 38.891,
        # # 'E': 0,
        "F": 46.249,
        "G": 51.913,
    },
    2: {
        "a": 110,
        "b": 123.471,
        "c": 65.406,
        "d": 73.416,
        "e": 82.407,
        "f": 87.307,
        "g": 97.999,
        "A": 116.541,
        # 'B': 0,
        "C": 69.296,
        "D": 77.782,
        # # 'E': 0,
        "F": 92.499,
        "G": 103.826,
    },
    3: {
        "a": 220,
        "b": 246.942,
        "c": 130.813,
        "d": 146.832,
        "e": 164.814,
        "f": 174.614,
        "g": 195.998,
        "A": 233.082,
        # 'B': 0,
        "C": 138.591,
        "D": 155.563,
        # 'E': 0,
        "F": 184.997,
        "G": 207.652,
    },
    4: {
        "a": 440,
        "b": 493.883,
        "c": 261.626,
        "d": 293.665,
        "e": 329.628,
        "f": 349.228,
        "g": 391.995,
        "A": 466.164,
        # 'B': 0,
        "C": 277.183,
        "D": 311.127,
        # 'E': 0,
        "F": 369.994,
        "G": 415.305,
    },
    5: {
        "a": 880,
        "b": 987.767,
        "c": 523.251,
        "d": 587.33,
        "e": 659.255,
        "f": 698.456,
        "g": 783.991,
        "A": 932.328,
        # 'B': 0,
        "C": 554.365,
        "D": 622.254,
        # 'E': 0,
        "F": 739.911,
        "G": 830.609,
    },
    6: {
        "a": 1760,
        "b": 1975.533,
        "c": 1046.502,
        "d": 1174.659,
        "e": 1318.51,
        "f": 1396.913,
        "g": 1567.982,
        "A": 1864.655,
        # 'B': 0,
        "C": 1108.731,
        "D": 1244.508,
        # 'E': 0,
        "F": 1479.978,
        "G": 1661.219,
    },
    # TODO: fill in 7, 8, and 9
}

dash_delay = 1 / 500
# dash_delay = 0

outfile = open(sys.argv[1], "wb") if len(sys.argv) > 1 else open("bad-beep", "wb")


def parse_line(line: str | None) -> tuple[str, str]:
    if not line:
        return "", ""
    octave = int(line[0])
    rest = line[2:-1]
    return octave, rest


def groups_of_n(iterable: Iterable, n: int) -> Iterable:
    return zip_longest(*[iter(iterable)] * n)


def notes_to_beeps():
    outfile.write(b"#/usr/bin/env bash\n")
    outfile.write(b"set -x\n")
    lines = music_notes.splitlines()
    for line1, line2 in groups_of_n(lines, 2):
        if not line1.strip():
            continue
        octave1, rest1 = parse_line(line1)
        octave2, rest2 = parse_line(line2)

        i = 0
        while i < len(rest1):
            dash_n = 0
            while i < len(rest1) and rest1[i] == "-":
                dash_n += 1
                i += 1
            if dash_delay and dash_n:
                outfile.write(bytes(f"sleep {dash_n * dash_delay}\n", encoding="utf-8"))
            if i < len(rest2) and rest2[i] != "-":
                # Try to play letters on the same column together. Not sure if this is working properly
                freq1 = conversion_table[octave1][rest1[i]]
                freq2 = conversion_table[octave2][rest2[i]]
                outfile.write(
                    bytes(
                        f"beep -f {freq1} &\nbeep -f {freq2} &\nwait\n",
                        encoding="utf-8",
                    )
                )
                i += 1
            elif i < len(rest1):
                freq = conversion_table[octave1][rest1[i]]
                outfile.write(bytes(f"beep -f {freq}\n", encoding="utf-8"))
                i += 1

        i = 0
        while i < len(rest2):
            dash_n = 0
            while i < len(rest2) and rest2[i] == "-":
                dash_n += 1
                i += 1
            if dash_delay and dash_n:
                outfile.write(bytes(f"sleep {dash_n * dash_delay}\n", encoding="utf-8"))
            elif i < len(rest2) and (len(rest1) >= i or rest1[i] == "-"):
                freq = conversion_table[octave2][rest2[i]]
                outfile.write(bytes(f"beep -f {freq}\n", encoding="utf-8"))
                i += 1


notes_to_beeps()
