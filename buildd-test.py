#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       buildd-test.py
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

import os
import pybitclient
from pybitclient.subversion import SubversionClient
from pybitclient.debian import DebianBuildClient
from pybitclient import PyBITClient
from pybit.models import BuildRequest, Transport, PackageInstance, Job, Arch, Suite, Package

def main():
	conffile = "%s/pybitclient/client.conf" % (os.getcwd());
	if os.path.isfile (conffile):
		options = pybitclient.get_settings(conffile)
	else :
		options = pybitclient.get_settings("/etc/pybit/client/client.conf")
	build_client = PyBITClient(options["host_arch"], "debian", "deb", "pybit", None)

	# Test One
	vcs_id = "21094"
	method_type = "svn"
	suite = "pybit"
	package = "pybit"
	version = "0.0.25"
	architecture = "i386"
	source = "pybit"
	uri = "http://svn/svn/lwdev/software/trunk/packages/pybit"

	test_arch = Arch(0, architecture)
	test_suite = Suite (0, suite)
	test_transport = Transport (0, method_type, uri, vcs_id)
	test_package = Package(0, version, package)
	test_packageinstance = PackageInstance(1, test_package, test_arch, test_suite, "deb", "debian", True)
	test_job =  Job(2, test_packageinstance,None)
	test_req = BuildRequest(test_job,test_transport,None)
	vcs = SubversionClient ()
	vcs.fetch_source (test_req, None)
	client = DebianBuildClient ()
	# To check the build-dependencies in advance, we need to ensure the
	# chroot has an update apt-cache, so can't use apt-update option of
	# sbuild. The alternative is to update the apt-cache twice per build,
	# once for the dep check and once before the build. The choice depends
	# on whether two network trips are more efficient than rewriting the
	# lvm snapshot before even trying to do any build.
	if options["use_lvm"] :
		name = suite + "-source"
	else:
		name = suite
	client.update_environment (name, test_req, None)
	while client.is_building() :
		wait(self)
	client.build_master (test_req, None)
	vcs.clean_source(test_req, None)
	vcs_id = ""
	package = "textparser"
	version = "0.0.13"
	architecture = "i386"
	source = "textparser"
	uri = "http://svn/svn/lwdev/software/trunk/packages/textparser"

	# test two
	test_arch = Arch(0, architecture)
	test_suite = Suite (0, suite)
	test_transport = Transport (0, method_type, uri, vcs_id)
	test_package = Package(0, version, package)
	test_packageinstance = PackageInstance(1, test_package, test_arch, test_suite, "deb", "debian", True)
	test_job =  Job(2, test_packageinstance,None)
	test_req = BuildRequest(test_job,test_transport,None)

	vcs.fetch_source (test_req, None)
	client.build_slave (test_req, None)
	vcs.clean_source(test_req, None)

	return 0

if __name__ == '__main__':
	main()

