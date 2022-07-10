#!/usr/bin/env python3
"""
This program and the accompanying materials are made available under the
terms of the Eclipse Public License 2.0, which is available at
http://www.eclipse.org/legal/epl-2.0, or the MIT License,
which is available at https://spdx.org/licenses/MIT.html.
"""

__author__ = "Mārtiņš Avots"
__authors__ = ["and other"]
__copyright__ = "Copyright 2021"
__license__ = "EPL-2.0 OR MIT"

import argparse
import logging
import subprocess
import sys

from os import environ

if __name__ == '__main__':
	if environ.get('log_level') == 'debug':
		logging.basicConfig(level = logging.DEBUG)
	parser = argparse.ArgumentParser()
	parser.add_argument('--remote-repo-name'
				, dest = 'remoteRepoName'
				, required = True
				, help = 'This is the local name of the remote repository,to which data is pushed.')
	parser.add_argument('--remote-repo-URL'
		, dest = 'remoteRepoUrl'
		, required = True
		, help = 'This is the URL of the remote repository,to which data is pushed.')
	parsedArgs = parser.parse_args()
	
	commandToExecute = "git remote add "\
				+ parsedArgs.remoteRepoName\
				+ " "\
				+ parsedArgs.remoteRepoUrl\
				+ " 2>/dev/null"
	logging.debug("Executing: Ensure that remote label exists: " + commandToExecute)
	subprocess.call(commandToExecute, shell='True') # The return code, of this command is irrelevant, because it is unequals 0, if the label is already present.

	
	commandToExecute = "git remote set-url "\
				+ parsedArgs.remoteRepoName\
				+ " "\
				+ parsedArgs.remoteRepoUrl\
				+ " 2>/dev/null"
	logging.debug("Executing: Set remote URL: " + commandToExecute)
	returnCode = subprocess.call(commandToExecute, shell='True')
	if returnCode != 0:
		exit(1)
	
	commandToExecute = "git remote set-url --push "\
				+ parsedArgs.remoteRepoName\
				+ " "\
				+ parsedArgs.remoteRepoUrl\
				+ " 2>/dev/null"
	logging.debug("Executing: Set remote URL: " + commandToExecute)
	returnCode = subprocess.call(commandToExecute, shell='True')
	if returnCode != 0:
		exit(1)
	
	commandToExecute = "git push --all " + parsedArgs.remoteRepoName
	logging.debug("Executing: Set remote URL: " + commandToExecute)
	returnCode = subprocess.call(commandToExecute, shell='True')
	if returnCode != 0:
		exit(1)