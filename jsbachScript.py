import os


def runJSBachScript(arxiu, partitura):
    createlilypondfile(arxiu, partitura)
    executelilypond(arxiu)
    executetimidity(arxiu)
    executeffmpeg(arxiu)
    executeffplay(arxiu)


def createlilypondfile(arxiu, partitura):
    file = open("./assets/template.lily", "r")
    list_lines = file.readlines()
    list_lines[4] = f"\t\t{partitura}\n"
    file.close()
    out_file = open(f"./assets/{arxiu}.lily", "w")
    out_file.writelines(list_lines)


def executelilypond(arxiu):
    print("·------------------------------------------------------------------------------·\n"
          "|                             EXECUTANT LILYPOND                               |\n"
          "·------------------------------------------------------------------------------·")
    stream = os.popen(f"cd assets && lilypond {arxiu}.lily")
    output = stream.read()
    print(output)


def executetimidity(arxiu):
    print("·------------------------------------------------------------------------------·\n"
          "|                           CONVERTINT .midi a .wav                            |\n"
          "·------------------------------------------------------------------------------·")
    stream = os.popen(f"timidity -Ow -o ./assets/{arxiu}.wav ./assets/{arxiu}.midi")
    output = stream.read()
    print(output)


def executeffmpeg(arxiu):
    print("·------------------------------------------------------------------------------·\n"
          "|                           CONVERTINT .wav a .mp3                             |\n"
          "·------------------------------------------------------------------------------·")
    stream = os.popen(f"ffmpeg -i ./assets/{arxiu}.wav -codec:a libmp3lame -qscale:a 2 ./assets/{arxiu}.mp3")
    output = stream.read()
    print(output)


def executeffplay(arxiu):
    print("·------------------------------------------------------------------------------·\n"
          "|                            REPRODUINT ARXIU .mp3                             |\n"
          "·------------------------------------------------------------------------------·")
    stream = os.popen(f"ffplay ./assets/{arxiu}.mp3")
    output = stream.read()
    print(output)
