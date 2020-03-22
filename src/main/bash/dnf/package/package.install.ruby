#!/usr/bin/env sh
set -e
run.and.show.if.failed "sudo dnf install -y ruby"
run.and.show.if.failed "sudo dnf install -y rubygems"
run.and.show.if.failed "sudo dnf install -y ruby-devel"
run.and.show.if.failed "sudo dnf install -y rubygems-devel"
run.and.show.if.failed "sudo dnf install -y rubygem-bundler"
