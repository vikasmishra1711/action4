print("trying to push code in aws")
print("ci/cd checking")
print("i think now it works")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 My CI/CD app is running on AWS EC2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
