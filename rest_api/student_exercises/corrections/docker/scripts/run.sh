# -d: means to run in background
# -p: means to expose port 8000
# --name: name of the container
# nomades_booksapi:latest: name of the image

docker container run -d -p 8000:5050 --name nomades_booksapi nomades_booksapi:latest