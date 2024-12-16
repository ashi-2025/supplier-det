# Dockerfile
FROM python:3.9-slim

# Install required packages
RUN pip install requests

# Copy the script
COPY fetch_suppliers.py /app/fetch_suppliers.py

# Set the working directory
WORKDIR /app

# Run the script
CMD ["python", "fetch_suppliers.py"]
