#!/usr/bin/env python
import json
import sys
from shutil import copyfile

if len(sys.argv) != 3:
  print('please specify a game key and a folder')
  exit(1)

game = sys.argv[1]
folder = sys.argv[2]

config_file_data = ''

with open(game+'/data.json', 'r') as config_file:
  all_config_file_data = json.loads(config_file.read())

for file_data in all_config_file_data:
  print('copying "' + folder + '/' + file_data['location'] + '" to "' + game + '/' + file_data['file'] + '"')
  copyfile(folder + '/' + file_data['location'],  game + '/' + file_data['file'])
