import argparse
import subprocess
import itertools
import os
import sys


parser = argparse.ArgumentParser()
parser.add_argument('pdf')
parser.add_argument('density')
args = parser.parse_args()

# Convert the pdf pages into jpgs
anki_directory = "/home/grey/.local/share/Anki2/User 1/collection.media"
directory = '/'.join(args.pdf.split('/')[0:-1])
output_name = args.pdf.split('/')[-1].split('.')[0]
code = subprocess.run(['convert', '-density', args.density, args.pdf, f"{directory}/{output_name}.jpg"])

if code.returncode != 0:
    print("Failed to convert files")
    sys.exit(-1)

# move the jpgs into Anki media folder
max_file_name = None
try:
    for i in itertools.count(0):
        file_name = f"{output_name}-{i}.jpg"
        os.replace(f"{directory}/{file_name}", f"{anki_directory}/{file_name}")

        max_file_name = i
except Exception as e:
    pass

# Output the html text to input into Anki
for i in range(0, max_file_name + 1):
    print(f"Slides {i+1}:<br /><img src=\"{output_name}-{i}.jpg\" /><br />", end='')
