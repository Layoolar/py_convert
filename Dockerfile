# Use the official Ubuntu image as the base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the required files into the container
COPY * ./

# Install system dependencies
RUN apt update && \
    apt install -y libreoffice python3 python3-pip unoconv && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install Flask

# Expose port 5000 for Flask application (if needed)
EXPOSE 5000

# Run the convert.py script
CMD ["python3", "doc.py"]
