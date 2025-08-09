#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-2.0-only
# SPDX-FileCopyrightText: Contributors To The `net.splitcells.*` Projects
if [  -n "$(uname -a | grep Ubuntu)" ]; then
	echo 1
else
	echo 0
fi  