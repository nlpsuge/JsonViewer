#!/usr/bin/env bash

shell_name="${BASH_SOURCE-$0}"
shell_name="$(dirname "${shell_name}")"
shell_basedir="$(cd "${shell_name}"; pwd)"
cd "$shell_basedir"

nohup python3 ../backend/app.py &
cd ../frontend/web/vue/ && nohup npm run serve &

