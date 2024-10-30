# A base for the container. By default fetching from DockerHub (hub.docker.com)
FROM ros:humble

# Create workspace folder and copy code in there
ENV WORKSPACE=/workspace
RUN mkdir -p $WORKSPACE/src
COPY src/ $WORKSPACE/src/

# Install turtlesim for visualization
RUN apt update && apt install -y ros-${ROS-DISTRO}-turtlesim

# Build our ros packages
RUN  cd ${WORKSPACE} && \
     . /opt/ros/$ROS_DISTRO/setup.sh && \
     colcon build

# Opening new terminals will now have workspace sourced
RUN echo '. /opt/ros/$ROS_DISTRO/setup.sh' >> ~/.bashrc && \
    echo '. $WORKSPACE/install/setup.bash' >> ~/.bashrc

COPY docker/ros_entrypoint.sh /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["bash"]
