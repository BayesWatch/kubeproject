# Building and Running docker containers

## Usage 

To use:

1. Build the image with 
   ```bash
   docker build -t <image_name> docker/<accelerator-type>/
   ```
2. Run the container with 
    ```bash
    docker run --gpus all --name <container-instance-name> --shm-size=12gb --env-file .env -v /container/mount/folder/:/machine/folder/to/mount/ -it <image_name>
    ```


 Have fun 😎
