FROM python:3.11-slim

RUN apt-get update && apt-get install -y xxd

WORKDIR /app

# Copy the deterministic random generator script
COPY generate_rand.py /app
COPY entrypoint.sh /app
RUN chmod +x /app/generate_rand.py
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["/bin/bash"]
