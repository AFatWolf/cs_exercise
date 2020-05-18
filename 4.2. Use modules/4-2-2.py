# Set of Yamanote Line stations
stations = {'ueno', 'shinjuku', 'akihabara', 'komagome', 'gotanda'}

while True:
  s = input('Station? ')
  if s not in stations:
    print('Game Over')
    break
	
  # Remove the name s used just now
  stations.remove(s)