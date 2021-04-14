from flask import Flask, render_template
from threading import Thread

app = Flask('')


@app.route('/running')
def main():
    return "Project Running! | Thanks For Using PeelyBot"

@app.route('/')
def projectrunning():
  return render_template('index.html')


if __name__ == "__main__":
  app.run()

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start() 
