import requests
import pygal
from pygal.style import LightColorizedStyle as lcs, LightenStyle as ls

# make a api call and store the request

url = 'https://api.github.com/search/repositories?q=language:python&python&sort=stars'
r = requests.get(url)
print("status code", r.status_code)

# store api response in a variable
response_dict = r.json()

# process results
print(response_dict.keys())

print("total repository count", response_dict['total_count'])
# explore information about the repositories
repo_dicts = response_dict['items']

names, plot_dicts = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
# make visualization
my_style = ls('#333366', base_style=lcs)

my_config = pygal.Config()

my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.tile_font_size = 24
my_config.label_font_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guifes = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'most stared python projects in git hub'
chart.x_labels = names

chart.add(' ', plot_dicts)
chart.render_to_file('git.svg')

#
# # print(repo_dicts)
#
#
# print("repositories returned",len(repo_dicts))
# # # print(response_dict.value)
# #
# # examine the first repository
# repo_dicts = repo_dicts[0]
# print("\nkeys:",len(repo_dicts))
# for key in sorted(repo_dicts.keys()):
#     print(key)
#
# print("selected information about first repository")
# for repo_dict in repo_dicts:
#     print('Name',repo_dicts['name'])
#     print('Owner',repo_dicts['owner']['login'])
#     print('Stars',repo_dicts['stargazers_count'])
#     print('Repository',repo_dicts['html_url'])
#     print('created',repo_dicts['created_at'])
#     print('updated',repo_dicts['updated_at'])
#     print('description',repo_dicts['description'])
