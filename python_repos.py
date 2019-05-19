import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

response_dict = r.json()
print('Total repositories:', response_dict['total_count'])
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

names, plot_dicts = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# Visualize
my_style = LS('#333366', base_style=LCS)

my_conf = pygal.Config()
my_conf.x_label_rotation = 45
my_conf.show_legend = False
my_conf.title_font_size = 24
my_conf.label_font_size = 14
my_conf.major_label_font_size = 18
my_conf.truncate_label = 15
my_conf.show_y_guides = False
my_conf.width = 1000

chart = pygal.Bar(my_conf, style=my_style)
chart.title = 'Most stared python projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos10.svg')
