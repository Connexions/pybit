#!/usr/bin/python

# TODO: Change DB methods and associated HTTP GEThandlers to work on these JSON objects, rather than returning the raw resultsets themselves, which are a pain to deserialise.

import jsonpickle


# new
class Model(object):
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

class JobHistory(Model):
	def __init__(self,job_id,status,buildclient,time):
		self.job_id = job_id
		self.status = status
		self.buildclient = buildclient
		self.time = str(time) #????

class ClientMessage:
	failed = "Failed"
	building = "Building"
	done = "Done"
	blocked = "Blocked"


class Arch(Model):
	def __init__(self,arch_id,name):
		self.id = arch_id
		self.name = name

class Dist(Model):
	def __init__(self,dist_id,name):
		self.id = dist_id
		self.name = name

class Format(Model):
	def __init__(self,format_id,name):
		self.id = format_id
		self.name = name

class Status(Model):
	def __init__(self,status_id,name):
		self.id = status_id
		self.name = name

class Suite(Model):
	def __init__(self,suite_id,name):
		self.id = suite_id
		self.name = name

class BuildD(Model):
	def __init__(self,buildd_id,name):
		self.id = buildd_id
		self.name = name

class Package(Model):
	def __init__(self,package_id,version,name):
		self.id = package_id
		self.version = version
		self.name = name

class Transport(Model) :
	def __init__(self,transport_id,method,uri,vcs_id):
		self.id = transport_id
		self.method = method
		self.uri = uri
		self.vcs_id = vcs_id

class PackageInstance(Model):
	def __init__(self, packageinstance_id, package, arch, suite, distribution, pkg_format, master) :
		self.id = packageinstance_id
		self.package = package
		self.arch = arch
		self.suite = suite
		self.distribution = distribution
		self.format = pkg_format
		self.master = master


class Job(Model):
	def __init__(self,job_id,packageinstance,buildclient):
		self.id = job_id
		self.packageinstance = packageinstance
		self.buildclient = buildclient


class SuiteArch(Model):
	def __init__(self,suitearch_id,suite_id,arch_id):
		self.id = suitearch_id
		self.suite_id = suite_id
		self.arch_id = arch_id


class BuildRequest(Model):
	def __init__(self,job,transport,web_host):
		self.job = job
		self.transport = transport
		self.web_host = web_host

	def get_suite(self):
		return self.job.packageinstance.suite.name

	def get_package(self):
		return self.job.packageinstance.package.name

	def get_version(self):
		return self.job.packageinstance.package.version

	def get_arch(self):
		return self.job.packageinstance.arch.name

class AMQPConnection(object):
	def __init__(self, client_name, host, userid, password, vhost, insist=False):
		self.client_name = client_name
		self.host = host
		self.userid = userid
		self.password = password
		self.vhost = vhost
		self.insist = insist
	def as_dict(self):
		return  dict( host=self.host, userid=self.userid, password=self.password,
			virtual_host=self.vhost, insist= False )
	def __repr__(self):
		return "host: %s user id:%s password:%s vhost:%s insist: %s" % (
			self.host, self.userid, self.password, self.vhost, self.insist) 
	


class CommandRequest(Model):
	def __init__(self,job,web_host):
		self.job = job
		self.web_host = web_host


class CancelRequest(CommandRequest):
	def  __init__(self,job,web_host):
		CommandRequest.__init__(self, job, web_host)


class StatusRequest(CommandRequest):
	def  __init__(self,job,web_host):
		CommandRequest.__init__(self, job, web_host)


class TaskComplete(Model):
	def __init__(self, message, success = True):
		self.success = success
		self.message = message

