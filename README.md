# ros_lecture_demo
A simple ros and docker demo to show in lectures. Tested on unix system. For windows the setup requires bit extra steps including installing WSL2 etc.

Contains an example of and publisher in python. Running the publisher nodes with turtlesim will visualize what the effect of publishers.

Note: This example has CMakeLists.txt approach for specifying the package. This will allow you to have python and cpp sources in same package.

# How to run

- You will need docker[https://docs.docker.com/engine/install/] (and optionally docker-compose[https://docs.docker.com/compose/install/]) installed on your machine

Before anything, add the following line to your `~/.bashrc` file, and then open a new terminal: `export LOCAL_ROS_WORKSPACE_PATH=<absolute_path_to_the_root_of_this_project>`. In my case, the value of that env variable is: `/home/george/workspaces/ros_lecture_demo`.

For gui following command is required to be ran on host machine `xhost +local:humble_sandbox`. (To remove the right from xhost run `xhost -local:humble_sandbox`)

- `git clone https://github.com/jonipol/ros_lecture_demo.git`
- `cd lecture_demo/docker`
- `bash build_image.bash`
- `docker run -it --name="humble_sandbox" --env="DISPLAY=$DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --runtime=nvidia humble_sandbox bash`

Or if you have docker-compose you can run
- `docker-compose up`

To open additional terminals `docker exec -it humble_sandbox bash`

Once the container is running you can run
- `ros2 run turtlesim turtlesim_node` in one terminal
- `ros2 run lecture_demo demo_publisher.py` in other terminal
Now you should be seeing the ros magic working.
