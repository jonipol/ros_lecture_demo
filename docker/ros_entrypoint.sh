#!/bin/bash
set -e  # This was causing Docker to exit when auto-filling or running into error

. "/opt/ros/${ROS_DISTRO}/setup.bash"
 . "$WORKSPACE/install/setup.bash"

exec "$@"
