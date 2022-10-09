# GATE-docker

## Usage 

To use:

1. Fill in the .env_template with your own values and rename it to .env
2. Build the image with `docker build -t <container_name> docker/<accelerator-type>/`
3. Run the container with `docker run --gpus all --name <container-instance-name> --shm-size=12gb --env-file .env -v /container/mount/folder/:/machine/folder/to/mount/ -it <container_name>`


🐈 Have fun.
