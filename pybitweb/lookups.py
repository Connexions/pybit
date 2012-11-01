#!/usr/bin/python

#       pybit-web
#       Copyright 2012:
#
#		Nick Davidson <nickd@toby-churchill.com>,
#		Simon Haswell <simonh@toby-churchill.com>,
#		Neil Williams <neilw@toby-churchill.com>,
#		James Bennet <github@james-bennet.com / James.Bennet@toby-churchill.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from bottle import Bottle,route,run,template,debug,HTTPError,response,error,redirect,request
import jsonpickle
from db import Database,myDb
from pybit.models import Arch,Dist,Format,Status,Suite,SuiteArch

@route('/arch', method='GET')
def get_arch():
	try:
		#return list of arches
		arches = myDb.get_arches()
		encoded = jsonpickle.encode(arches)
		response.content_type = "application/json"
		return encoded
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/arch/<arch_id:int>', method='GET')
def get_arch_id(arch_id):
	try:
		# Returns all information about a specific arch
		res = myDb.get_arch_id(arch_id)

		# check results returned
		if res:
			encoded = jsonpickle.encode(res)
			response.content_type = "application/json"
			return encoded
		else:
			response.status = "404 - No arch found with this ID."
			return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/arch', method='POST')
@route('/arch', method='PUT')
def put_arch():
	try:
		# Add a new arch. TODO: TESTME
		name = request.forms.get('name')

		if name:
			myDb.put_arch(name)
		else:
			response.status = "400 - Required fields missing."
		return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/suitearch', method='GET')
def get_suitearch():
	try:
		#return list of suitearch
		suitearches = myDb.get_suitearches()
		encoded = jsonpickle.encode(suitearches)
		response.content_type = "application/json"
		return encoded
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/suitearch/<suitearch_id:int>', method='GET')
def get_suitearch_id(suitearch_id):
	try:
		# Returns all information about a specific suitearch
		res = myDb.get_suitearch_id(suitearch_id)

		# check results returned
		if res:
			encoded = jsonpickle.encode(res)
			response.content_type = "application/json"
			return encoded
		else:
			response.status = "404 - No suitearch found with this ID."
			return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/suitearch', method='POST')
@route('/suitearch', method='PUT')
def put_suitearch():
	try:
		# Add a new suitearch. TODO: TESTME
		suite_id = request.forms.get('suite_id')
		arch_id =  request.forms.get('arch_id')

		if suite_id and arch_id:
			myDb.put_suitearch(suite_id,arch_id)
		else:
			response.status = "400 - Required fields missing."
		return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/status', method='GET')
def get_statuses():
	try:
		#return list of statuses
		statuses = myDb.get_statuses()
		encoded = jsonpickle.encode(statuses)
		response.content_type = "application/json"
		return encoded
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/status/<status_id:int>', method='GET')
def get_status_id(status_id):
	try:
		# Returns all information about a specific status
		res = myDb.get_status_id(status_id)

		# check results returned
		if res:
			encoded = jsonpickle.encode(res)
			response.content_type = "application/json"
			return encoded
		else:
			response.status = "404 - No status found with this ID."
			return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/status', method='POST')
@route('/status', method='PUT')
def put_status():
	try:
		# Add a new status. TODO: TESTME
		name = request.forms.get('name')

		if name:
			myDb.put_status(name)
		else:
			response.status = "400 - Required fields missing."
		return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/dist', method='GET')
def get_dists():
	try:
		#return list of distributions
		dists = myDb.get_dists()
		encoded = jsonpickle.encode(dists)
		response.content_type = "application/json"
		return encoded
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/dist/<dist_id:int>', method='GET')
def get_dist_id(dist_id):
	try:
		# Returns all information about a specific dist
		res = myDb.get_dist_id(dist_id)

		# check results returned
		if res:
			encoded = jsonpickle.encode(res)
			response.content_type = "application/json"
			return encoded
		else:
			response.status = "404 - No dist found with this ID."
			return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/dist', method='POST')
@route('/dist', method='PUT')
def put_dist():
	try:
		# Add a new dist. TODO: TESTME
		name = request.forms.get('name')

		if name:
			myDb.put_dist(name)
		else:
			response.status = "400 - Required fields missing."
		return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/format', method='GET')
def get_formats():
	try:
		#return list of package formats
		formats = myDb.get_formats()
		encoded = jsonpickle.encode(formats)
		response.content_type = "application/json"
		return encoded
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/format/<format_id:int>', method='GET')
def get_format_id(format_id):
	try:
		# Returns all information about a specific format
		res = myDb.get_format_id(format_id)

		# check results returned
		if res:
			encoded = jsonpickle.encode(res)
			response.content_type = "application/json"
			return encoded
		else:
			response.status = "404 - No format found with this ID."
			return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/format', method='POST')
@route('/format', method='PUT')
def put_format():
	try:
		# Add a new format. TODO: TESTME
		name = request.forms.get('name')

		if name:
			myDb.put_format(name)
		else:
			response.status = "400 - Required fields missing."
		return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/suite', method='GET')
def get_suites():
	try:
		#return list of suites
		suites = myDb.get_suites()
		encoded = jsonpickle.encode(suites)
		response.content_type = "application/json"
		return encoded
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/suite/<suite_id:int>', method='GET')
def get_suite_id(suite_id):
	try:
		# Returns all information about a specific suite
		res = myDb.get_suite_id(suite_id)

		# check results returned
		if res:
			encoded = jsonpickle.encode(res)
			response.content_type = "application/json"
			return encoded
		else:
			response.status = "404 - No suite found with this ID."
			return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None

@route('/suite', method='POST')
@route('/suite', method='PUT')
def put_suite():
	try:
		# Add a new suite. TODO: TESTME
		name = request.forms.get('name')

		if name:
			myDb.put_suite(name)
		else:
			response.status = "400 - Required fields missing."
		return
	except Exception as e:
		raise Exception('Exception encountered: ' + str(e))
		return None