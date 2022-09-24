import requests

def get_superheros_intelligence(superhero_name):
  url = "https://superheroapi.com/api/2619421814940190/search/" + superhero_name
  response = requests.get(url)
  posts = response.json()['results']

  for post in posts:
    if post['name'] == superhero_name:
      return int(post['powerstats']['intelligence'])

def print_max_superheros(superheros_dict):
  max_value = superheros_dict.get(max(superheros_dict))
  for hero, intelligence in superheros_dict.items():
    if intelligence == max_value:
      print(f'Самый умный: {hero}({intelligence})')

superheros_intelligence = {'Hulk': get_superheros_intelligence('Hulk'),
                           'Captain America': get_superheros_intelligence('Captain America'),
                           'Thanos': get_superheros_intelligence('Thanos')}

print_max_superheros(superheros_intelligence)