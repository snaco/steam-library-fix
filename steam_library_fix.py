import os
from shutil import copytree

# library_path = '/home/james/Games/SteamLibrary/steamapps/'
# local_path = '/home/james/.steam/external-library/steamapps/'
library_path = os.environ.get('STEAM_EXT_LIB')
local_path = os.environ.get('STEAM_LOC_LIB')

library_files = os.listdir(library_path)
if not library_path.endswith('/'):
  library_path += '/'
if not local_path.endswith('/'):
  local_path += '/'
library_games = os.listdir(f'{library_path}common/')
library_compat_data = os.listdir(f'{library_path}compatdata/')
library_acf_files = set(filter(lambda x: '.acf' in x, library_files))

local_file = os.listdir(local_path)
local_games = os.listdir(f'{local_path}common/')
local_compat_data = os.listdir(f'{local_path}compatdata/')
local_acf_files = set(filter(lambda x: '.acf' in x, library_files))

acf_files_delta = list(library_acf_files - local_acf_files)
game_delta = list(set(library_games) - set(local_games))

if not game_delta:
  print('All steam games ready to play, no patching required')
  exit()

#pre-migration logging
print('Current games ready to play:')
for game in local_games:
  print(f'\t{game}')
print('Games to patch:')
for game in game_delta:
  print(f'\t{game}')
print()

#link acf files
for acf_file in library_acf_files:
  if acf_file in local_acf_files:
    continue
  os.symlink(f'{library_path}{acf_file}', f'{local_path}{acf_file}')

#transfer compatdata
for compat_data_dir in library_compat_data:
  if compat_data_dir in local_compat_data:
    continue
  local_compat_dir = f'{local_path}compatdata/{compat_data_dir}/'
  library_compat_dir = f'{library_path}compatdata/{compat_data_dir}/'
  copytree(library_compat_dir, local_compat_dir)

#link game directories
for game in library_games:
  if game in local_games:
    continue
  os.symlink(f'{library_path}common/{game}', f'{local_path}common/{game}', target_is_directory=True)

print('Congratulations your steam library should now be playable!')