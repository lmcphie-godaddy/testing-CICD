CICD Challenge 2:
 
	Install Docker, pull ubuntu:latest image, run ubuntu image container in interactive mode, and then run ls.
    Research into Dockerfile, create Dockerfile that have following attributes:
	    Base Image : debian  version 11.
        Perform apt update & apt upgrade to patch the operating system.
        Change user to your name
        Create new file called test.txt in home directory.
        Run ls when container starts.
	Try building your Dockerfile & run the image on your computer.
    Now do the build & run in github action workflow.   