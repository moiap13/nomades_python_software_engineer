# For this container we want to use an ubuntu machine; 
# The same as the one used for the virtualbox virtual machine
FROM ubuntu:22.04

# We install some dependencies such as python and pip
RUN apt update -y \
  && apt install software-properties-common -y \
  && add-apt-repository ppa:deadsnakes/ppa \
  && apt install python3.10 pip -y

# We create a working directory (main directory inside the container)
WORKDIR /app

# We copy the folder that containes our app inside the container
COPY ./booksAPI /app/booksAPI

# We expose the port 5050 
# -> this mean we want to use port 5050 of the container outside the container
# Here the port 5050 is the port used by flask
EXPOSE 5050

# We install the requirements for python
# The requirements.txt contains all the dependencies we need to run the app properly
RUN pip install -r booksAPI/requirements.txt

# We run the app, as the default command
CMD ["python3.10", "booksAPI/app.py"]
