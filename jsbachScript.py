import os
import shutil


def runJSBachScript(arxiu, partitura):
    createlilypondfile(arxiu, partitura)
    executelilypond(arxiu)
    executetimidity(arxiu)
    executeffmpeg(arxiu)
    executeffplay(arxiu)


def createlilypondfile(arxiu, partitura):
    file = open("template.lily", "r")
    list_lines = file.readlines()
    list_lines[4] = "\t\t" + partitura + "\n"
    file = open("template.lily", "w")
    file.writelines(list_lines)
    file.close()
    shutil.copyfile("template.lily", f"{arxiu}.lily")
    resettemplate()


def resettemplate():
    file = open("template.lily", "r")
    list_lines = file.readlines()
    list_lines[4] = "\n"
    file = open("template.lily", "w")
    file.writelines(list_lines)
    file.close()


def executelilypond(arxiu):
    print("·------------------------------------------------------------------------------·\n"
          "|                             EXECUTANT LILYPOND                               |\n"
          "·------------------------------------------------------------------------------·")
    stream = os.popen(f"lilypond {arxiu}.lily")
    output = stream.read()
    print(output)


def executetimidity(arxiu):
    print("·------------------------------------------------------------------------------·\n"
          "|                           CONVERTINT .midi a .wav                            |\n"
          "·------------------------------------------------------------------------------·")
    stream = os.popen(f"timidity -Ow -o {arxiu}.wav {arxiu}.midi")
    output = stream.read()
    print(output)


def executeffmpeg(arxiu):
    print("·------------------------------------------------------------------------------·\n"
          "|                           CONVERTINT .wav a .mp3                             |\n"
          "·------------------------------------------------------------------------------·")
    stream = os.popen(f"ffmpeg -i {arxiu}.wav -codec:a libmp3lame -qscale:a 2 {arxiu}.mp3")
    output = stream.read()
    print(output)


def executeffplay(arxiu):
    print("·------------------------------------------------------------------------------·\n"
          "|                            REPRODUINT ARXIU .mp3                             |\n"
          "·------------------------------------------------------------------------------·")
    stream = os.popen(f"ffplay {arxiu}.mp3")
    output = stream.read()
    print(output)
