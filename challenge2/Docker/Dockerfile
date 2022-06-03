# Base Image
FROM debian:11

# patch the operating system
RUN apt-get update && apt-get upgrade -y 

# Create the user & Change user to your name

    # RUN adduser leandra
    # WORKDIR /home/leandra
    # USER leandra
    # RUN touch test.txt

ARG USERNAME=leandra
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}

USER leandra

# Create new file in home directory
WORKDIR /home/leandra
RUN touch test.txt

# Run ls when container starts
CMD ls -al
