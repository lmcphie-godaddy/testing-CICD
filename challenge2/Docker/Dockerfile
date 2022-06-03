# Base Image
FROM debian:11
# WORKDIR /testing-CICD/challenge2/Docker

# patch the operating system
RUN apt-get update && apt-get upgrade -y 

# Create the user & Change user to your name
ARG USERNAME=leandra
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME 

# USER $USERNAME

# Create new file in home directory
WORKDIR /home
RUN touch /home/test.txt

# Run ls when container starts
RUN ls  

CMD ["echo", "Hello World!"]