FROM ros:humble

ENV WORKSPACE=/workspace
RUN mkdir -p $WORKSPACE/src
COPY src/ $WORKSPACE/src/

RUN apt update && apt install -y ros-humble-turtlesim

RUN  cd ${WORKSPACE} && \
     . /opt/ros/$ROS_DISTRO/setup.sh && \
     colcon build

# Needed so that exec always sources ros_entrypoint
RUN echo '. /opt/ros/$ROS_DISTRO/setup.sh' >> ~/.bashrc && \
    echo '. $WORKSPACE/install/setup.bash' >> ~/.bashrc

COPY docker/ros_entrypoint.sh /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
