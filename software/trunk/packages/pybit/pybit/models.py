#!/usr/bin/python

# TODO: Change DB methods and associated HTTP GEThandlers to work on these JSON objects, rather than returning the raw resultsets themselves, which are a pain to deserialise.

import jsonpickle

# new
class model(object):
	def toJson(self):
		try:
			return jsonpickle.encode(self)
		except Exception as e:
			raise Exception('Error in toJson(): ' + str(e))
			return None
	def fromJson(self,jsonstring):
		try:
			self = jsonpickle.decode(jsonstring)
			return self
		except Exception as e:
			raise Exception('Error in fromJson(): ' + str(e))
			return None

class arch(model):

	def __init__(self,id,name):
		self.id = id
		self.name = name

class dist(model):

	def __init__(self,id,name):
		self.id = id
		self.name = name

class format(model):

	def __init__(self,id,name):
		self.id = id
		self.name = name

class status(model):

	def __init__(self,id,name):
		self.id = id
		self.name = name

class suite(model):

	def __init__(self,id,name):
		self.id = id
		self.name = name

class buildd(model):

	def __init__(self,id,name):
		self.id = id
		self.name = name

class package(model):

	def __init__(self,id,version,name):
		self.id = id
		self.version = version
		self.name = name

class transport(model) :

	def __init__(self,id,method,uri,vcs_id):
		self.id = id
		self.method = method
		self.uri = uri
		self.vcs_id = vcs_id

class packageinstance(model):

	def __init__(self, id, package, arch, suite, distribution, format, master) :
		self.id = id
		self.package = package
		self.arch = arch
		self.suite = suite
		self.distribution = distribution
		self.format = format
		self.master = master

class job(model):

	def __init__(self,id,packageinstance,buildclient):
		self.id = id
		self.packageinstance = packageinstance
		self.buildclient = buildclient

class suitearch(model):

	def __init__(self,id,suite_id,arch_id):
		self.id = id
		self.suite_id = suite_id
		self.arch_id = arch_id

class buildRequest(model):

	def __init__(self,job,transport,web_host):
		self.job = job
		self.transport = transport
		self.web_host = web_host
