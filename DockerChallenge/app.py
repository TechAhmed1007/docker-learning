from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_client = redis.Redis(host=redis_host, port=6379, decode_responses=True)


@app.route("/")
def home():
    return "Welcome to the Docker Container Challenge!"


@app.route("/count")
def count():
    visits = redis_client.incr("visits")
    return f"Visit count: {visits}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)