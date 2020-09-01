#!/usr/bin/env bash
# User Friendly Shell: https://fishshell.com/docs/current/design.html
if [ "1" -eq "$(system.is.Ubuntu)" ]; then
	set -x # Exit on first error.
	sudo apt-add-repository -y ppa:fish-shell/release-3
	sudo apt-get update -y
	sudo apt-get install -y fish
else
	exit 1
fi
