# Base image
FROM python:3.9

# Working directory
WORKDIR /app

# Copy HTML file
COPY index.html .

# Expose port
EXPOSE 8000

# Start HTTP Server
CMD ["python", "-m", "http.server", "8000"]
