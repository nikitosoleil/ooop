import json

def get_config(json_file_path):
	with open(json_file_path, 'r') as json_file:
		config = json.loads(json_file.read())
	config['checkpoint'] = '../experiments/' + config['experiment'] + '/checkpoint/'
	config['summary'] = '../experiments/' + config['experiment'] + '/summary/'
	return config