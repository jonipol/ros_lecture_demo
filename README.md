# ros_lecture_demo
A simple ros and docker demo to show in lectures

# How to run

- You will need docker and docker-compose installed on your machine (Can be ran without compose but requires you to write the command manually)
- Your system must have environment variable `LECTURE_DEMO_PATH` set. To set run `export LEXTURE_DEMO_PATH=<path/to/lecture_demo/

For gui following command is required `xhost +local:root`. NOTE: This is not the safest option!
- `cd docker`
- `bash build_image.bash`
- `docker-compose up`

To open additional terminals `docker exec -it lecture_demo bash`
