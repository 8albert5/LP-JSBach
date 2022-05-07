import os
import sys

# Eliminem l'extensió .lily
arxiu = sys.argv[1][:-5]

print("·------------------------------------------------------------------------------·\n"
      "|                             EXECUTANT LILYPOND                               |\n"
      "·------------------------------------------------------------------------------·")
stream = os.popen(f"lilypond {arxiu}.lily")
output = stream.read()
print(output)

print("·------------------------------------------------------------------------------·\n"
      "|                           CONVERTINT .midi a .wav                            |\n"
      "·------------------------------------------------------------------------------·")
stream = os.popen(f"timidity -Ow -o {arxiu}.wav {arxiu}.midi")
output = stream.read()
print(output)

print("·------------------------------------------------------------------------------·\n"
      "|                           CONVERTINT .wav a .mp3                             |\n"
      "·------------------------------------------------------------------------------·")
stream = os.popen(f"ffmpeg -i {arxiu}.wav -codec:a libmp3lame -qscale:a 2 {arxiu}.mp3")
output = stream.read()
print(output)

print("·------------------------------------------------------------------------------·\n"
      "|                            REPRODUINT ARXIU .mp3                             |\n"
      "·------------------------------------------------------------------------------·")
stream = os.popen(f"ffplay {arxiu}.mp3")
output = stream.read()
print(output)
