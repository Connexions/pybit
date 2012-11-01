#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       buildclient.py
#
#       Copyright 2012 Neil Williams <codehelp@debian.org>
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

import pybitclient
import pybit

class VersionControlHandler(object):
	def fetch_source(self):
		pass

	def get_srcdir (self):
		pass

	def clean_source (self, pkg) :
		pass

	# support test cases
	def is_dry_run (self):
		if (not hasattr(self, 'options')) :
			return False
		if (not "dry_run" in self.options) :
			return False
		return self.options["dry_run"]

	def __init__(self):
		self.workdir = ""
		self.options = {}
		try:
			self.options =  pybit.load_settings("client.conf")
			if not "dry_run" in self.options:
				self.options["dry_run"] = True
			if not "buildroot" in self.options:
				self.options["buildroot"] = "/tmp/buildd"
		except Exception as e:
			raise Exception('Error constructing subversion build client: ' + str(e))
			return

class PackageHandler(object):

	chan = None

	def __init__(self):
		self.build_process = None
		try:
			self.options = pybit.load_settings("client.conf")
			if not "dry_run" in self.options:
				self.options["dry_run"] = True
			if not "buildroot" in self.options:
				self.options["buildroot"] = "/tmp/buildd"
		except Exception as e:
			raise Exception('Error constructing subversion build client: ' + str(e))
			return
		return

	def is_dry_run (self):
		if (not hasattr(self, 'options')) :
			return False
		if (not "dry_run" in self.options) :
			return False
		return self.options["dry_run"]

	def build_master (self, buildroot):
		pass

	def build_slave (self, buildroot):
		pass

	def update_environment (self,name,pkg) :
		pass

	def upload (self, dirname, changes, pkg) :
		pass

	def is_building (self) :
		if not self.build_process :
			return False
		if self.build_process.poll() == None :
			return False
		return True

	def cancel (self) :
		try:
			if not self.build_process :
				return
			if self.build_process.poll() == None : # None if still running
				self.build_process.terminate()
		except Exception as e:
			raise Exception('Error cancelling: ' + str(e))
			return