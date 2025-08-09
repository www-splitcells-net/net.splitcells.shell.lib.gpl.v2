#!/usr/bin/env sh
# SPDX-License-Identifier: GPL-2.0-only
# SPDX-FileCopyrightText: Contributors To The `net.splitcells.*` Projects
set -e
sudo dnf install -y ruby
sudo dnf install -y rubygems
sudo dnf install -y ruby-devel
sudo dnf install -y rubygems-devel
sudo dnf install -y rubygem-bundler
