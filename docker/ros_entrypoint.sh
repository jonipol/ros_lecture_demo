#!/bin/bash
set -e  # This was causing Docker to exit when auto-filling or running into error

. "/opt/ros/${ROS_DISTRO}/setup.bash"
. "$PACKAGE_WORKSPACE/install/setup.bash"
. "$MAIN_WORKSPACE/install/setup.bash"

exec "$@"
