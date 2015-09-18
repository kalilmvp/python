class DataTable:
	""" Representa uma Tabela de dados

	Atributos:
	   nome
	   columns
	   data
	"""  


	def __init__(self, name):
		self._name = name
		self._columns = []
		self._data = []
		self._references = []
		self._referenced = []


	def add_column(self, name, kind, description):
		column = Column(name, kind, description)

		self.columns.append(column)

		return column

	def add_references(self, name, to, on):
		"""
			Cria uma referência dessa tabela para outra
		"""

		relationship = Relationship(name, self, to, on)
		self._references.append(relationship)

	def add_referenced(self, name, by, on):
		"""
			Cria uma referência para outra tabela que aponta para essa
		"""

		relationship = Relationship(name, by, self, on)
		self._referenced.append(relationship)

from decimal import Decimal

class Column:
	""" Representa uma Coluna

	Atributos:
	   nome
	   kind
	   description
	"""  

	def __init__(self, name, kind, description = ''):
		self._name = name
		self._kind = kind
		self._description = description
		self._is_pk = False

	def __str__(self):
		_str = "Col {} - Kind: {} - Description: {}".format(self._name, self._kind, self._description)
		return _str;

	def _validate(kind, data):
		if kind == 'bigint':
			if isinstance(data, int):
				return True
			return False
		elif kind == 'numeric':
			try:
				val = Decimal(data)
			except:
				return False
			return True
		elif kind == 'varchar':
			if isinstance(data, str):
				return True
			return False	

	validate = staticmethod(_validate)


class Relationship:
	""" Representa um relacionamento entre DataTables

	Atributos:
	   nome
	   kind
	   description
	"""  

	def __init__(self, name, _from, to, on):
		self._name = name
		self._from = _from
		self._to = to
		self._on = on

class PrimaryKey(Column):
	def __init__(self, table, name, kind, description = ''):
		super().__init__(name, kind, description = description)
		self._is_pk = True

	def __str__(self):
		_str = "Col {} - Kind: {} - Description: {}".format(self._name, self._kind, self._description)
		return "{} - {}".format('PK', _str);



