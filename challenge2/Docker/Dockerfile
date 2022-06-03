# Base Image
FROM debian:11

# patch the operating system
RUN apt-get update && apt-get upgrade -y 

# Create the user & Change user to your name
# Create new file in home directory
RUN adduser leandra
RUN touch /home/test.txt
USER leandra

    # ARG USERNAME=leandra
    # ARG USER_UID=1000
    # ARG USER_GID=${USER_UID}

    # RUN groupadd --gid ${USER_GID} ${USERNAME} \
    #     && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}

    # USER leandra

# Run ls when container starts
CMD ls -al