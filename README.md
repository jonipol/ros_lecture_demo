# ros_lecture_demo
A simple ros and docker demo to show in lectures. Tested on unix system. For windows the setup requires bit extra steps including installing WSL2 etc.

Contains an example of and publisher in python. Running the publisher nodes with turtlesim will visualize what the effect of publishers.

Note: This example has CMakeLists.txt approach for specifying the package. This will allow you to have python and cpp sources in same package.

# How to run

- You will need docker[https://docs.docker.com/engine/install/] (and optionally docker-compose[https://docs.docker.com/compose/install/]) installed on your machine


For gui following command is required to be ran on host machine `xhost +local:lecture_demo`. (To remove the right from xhost run `xhost -local:lecture_demo`)

- `git clone https://github.com/jonipol/ros_lecture_demo.git`
- `cd lecture_demo/docker`
- `bash build_image.bash`
- `docker run -it --name="lecture_demo" --env="DISPLAY=$DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --runtime=nvidia lecture_demo bash`

Or if you have docker-compose you can run
- `docker-compose up`

To open additional terminals `docker exec -it lecture_demo bash`

Once the container is running you can run
- `ros2 run turtlesim turtlesim_node` in one terminal
- `ros2 run lecture_demo demo_publisher.py` in other terminal
Now you should be seeing the ros magic working.
