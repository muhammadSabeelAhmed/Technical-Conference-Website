from flask import Flask, render_template

app = Flask(__name__)

# Dummy Data for Google Cloud Technologies Event
talks = [
    {
        "id": 1,
        "title": "Keynote: The Future of Cloud AI",
        "speakers": [{"first_name": "Sundar", "last_name": "Pichai", "linkedin": "https://linkedin.com/in/sundarpichai"}],
        "category": "1",
        "description": "Opening keynote on Google's vision for AI in the cloud.",
        "time": "09:00 - 09:45"
    },
    {
        "id": 2,
        "title": "Building Scalable Apps with Kubernetes",
        "speakers": [{"first_name": "Kelsey", "last_name": "Hightower", "linkedin": "https://linkedin.com/in/kelseyhightower"}],
        "category": "2",
        "description": "Deep dive into best practices for deploying applications to GKE.",
        "time": "09:50 - 10:35"
    },
    {
        "id": 3,
        "title": "Serverless Architectures on GCP",
        "speakers": [{"first_name": "Bret", "last_name": "McGowen", "linkedin": "https://linkedin.com/in/bretmcgowen"}],
        "category": "1",
        "description": "Exploring Cloud Run, Cloud Functions, and Eventarc.",
        "time": "10:45 - 11:30"
    },
    {
        "id": 4,
        "title": "Data Engineering with BigQuery",
        "speakers": [{"first_name": "Felipe", "last_name": "Hoffa", "linkedin": "https://linkedin.com/in/felipehoffa"}],
        "category": "2",
        "description": "Advanced analytics and data warehousing at petabyte scale.",
        "time": "11:35 - 12:20"
    },
    {
        "id": "lunch",
        "title": "Lunch Break",
        "speakers": [],
        "category": "",
        "description": "Networking lunch and partner exposition.",
        "time": "12:20 - 13:20"
    },
    {
        "id": 5,
        "title": "Modernizing Legacy Systems with Anthos",
        "speakers": [{"first_name": "Aparna", "last_name": "Sinha", "linkedin": "https://linkedin.com/in/aparnasinha"}, {"first_name": "Chen", "last_name": "Goldberg", "linkedin": "https://linkedin.com/in/chengoldberg"}],
        "category": "1",
        "description": "Strategies for hybrid and multi-cloud transformations.",
        "time": "13:20 - 14:05"
    },
    {
        "id": 6,
        "title": "Security Command Center Deep Dive",
        "speakers": [{"first_name": "Sunil", "last_name": "Potti", "linkedin": "https://linkedin.com/in/sunilpotti"}],
        "category": "2",
        "description": "Protecting your GCP environment from emerging threats.",
        "time": "14:10 - 14:55"
    },
    {
        "id": 7,
        "title": "Machine Learning with Vertex AI",
        "speakers": [{"first_name": "Cassie", "last_name": "Kozyrkov", "linkedin": "https://linkedin.com/in/cassiekozyrkov"}],
        "category": "1",
        "description": "End-to-end ML ops, training, and deployment.",
        "time": "15:05 - 15:50"
    },
    {
        "id": 8,
        "title": "Closing Panel: Ask the Experts",
        "speakers": [{"first_name": "Thomas", "last_name": "Kurian", "linkedin": "https://linkedin.com/in/thomaskurian"}],
        "category": "2",
        "description": "Q&A session with GCP product leads and engineers.",
        "time": "15:55 - 16:40"
    }
]

@app.route('/')
def index():
    return render_template('index.html', talks=talks)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
