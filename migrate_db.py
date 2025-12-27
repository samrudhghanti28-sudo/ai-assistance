from web_app import app
from models import db

def migrate_data():
    # This is a one-time migration script
    import json
    from pathlib import Path
    
    feedback_file = Path('feedback_log.jsonl')
    if feedback_file.exists():
        with open(feedback_file) as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    append_feedback(data)
        print("Migration completed!")
    else:
        print("No feedback file found to migrate")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        migrate_data()