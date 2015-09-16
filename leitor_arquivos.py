import os

def extract_entity_name(filename):
	return filename.split('.')[0]

def read_lines(filename):
	path_meta_data = 'data/meta-data'

	_file = open(os.path.join(path_meta_data, filename))

	data = _file.read().split('\n')

	return data

def read_meta_data(filename):
	meta_data = []

	for column in read_lines(filename):
		if column:
			meta_data.append(tuple(column.split('\t')))

	return meta_data

def prompt():
	print('\n O que deseja ver? ')
	print('(l) Listar entidades? ')
	print('(d) Exibir atributos de uma entidade? ')
	print('(r) Exibir referências de uma entidade? ')
	print('(s) Sair do programa? ')
	return input('')

def main():
	# dicionario nome entidade -> atributos
	meta = {}

	# dicionario identificador -> nome entidade
	keys = {}

	# dicionario de relacionamentos
	relationships = {}

	path_meta_data = 'data/meta-data'
	
	for meta_file in os.listdir(path_meta_data):
		table_name = extract_entity_name(meta_file)
		attributes = read_meta_data(meta_file)
		identifier = attributes[0][0]

		meta[table_name] = read_meta_data(meta_file)
		keys[identifier] = table_name

	for key, val in meta.items():
		#print('Entidade: {}'.format(key))
		#print('Atributos: ')

		for col in val:
			#print(' {}: {}'.format(col[1], col[0]))
			if col[0] in keys:
				if not col[0] == meta[key][0][0]:
					relationships[key] = keys[col[0]]
					#print('Entidade {} -> {}'.format(key, col[0]))

	opcao = prompt()

	while opcao != 's':
		if opcao == 'l':
			for entity_name in meta.keys():
				print(entity_name)
		elif opcao == 'd':
			entity_name = input('Nome da entidade? ')

			for col in meta[entity_name]:
				print(col)
		elif opcao == 'r':
			entity_name = input('Nome da entidade? ')
			other_entity = relationships[entity_name]

			print(other_entity)
		else:
			print('Inexistente...')

		opcao = prompt()


if __name__ == '__main__':
	main()





