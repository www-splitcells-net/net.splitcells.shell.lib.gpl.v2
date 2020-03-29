#!/usr/bin/env bash
# Worked on Ubuntu and may work in Debian.
set -e
run.and.show.if.failed "sudo apt install -y ruby"
run.and.show.if.failed "sudo apt install -y ruby-dev"