#!/usr/bin/env bash
set -e
sudo dnf install -y ruby
sudo dnf install -y rubygems
sudo dnf install -y ruby-devel
sudo dnf install -y rubygems-devel
sudo dnf install -y rubygem-bundler
