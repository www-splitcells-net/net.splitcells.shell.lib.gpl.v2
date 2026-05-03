#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-2.0-only
# SPDX-FileCopyrightText: Contributors To The `net.splitcells.*` Projects
set -e
if [ 'true' == $(repo.is.instance.of.git) ]; then
	git remote update origin
  # TODO Update all branches.
  git submodule update --recursive --remote
  git pull --no-edit origin
  exit $?
else
	exit 1
fi
