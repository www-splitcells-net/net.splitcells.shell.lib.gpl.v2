#!/usr/bin/env bash
if [  -n "$(uname -a | grep Ubuntu)" ]; then
	echo 1
else
	echo 0
fi  