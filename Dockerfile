FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the required files into the container
COPY convert.py pp.pptx ./

# Install system dependencies
RUN libreoffice unoconv

RUN curl -sSL https://bootstrap.pypa.io/get-pip.py | python3

# Install Python packages
RUN pip install Flask

# Expose port 5000 for Flask application (if needed)
EXPOSE 5000

# Run the convert.py script
CMD ["python3", "convert.py"]
