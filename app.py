from flask import Flask

app = Flask(__name__)
def init_db():
    for i in range(10):
        try:
            conn = get_conn()
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS visitors (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    message TEXT,
                    visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            conn.close()
            return
        except Exception as e:
            print(f"DB not ready, retrying ({i+1}/10)... {e}")
            time.sleep(3)

@app.route("/")
def hello():
    return "<h1>Hello from Docker on EC2!------re---------last</h1><p>Running inside a container on AWS.</p>"

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)