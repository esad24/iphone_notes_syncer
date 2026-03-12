from flask import Flask, request
import datetime         
import os
import json

app = Flask(__name__)

NOTES_JSON_PATH = "data/notes_json/notes.json"

@app.route('/upload-notes', methods=['POST'])
def upload_notes():
    raw_text = request.data.decode('utf-8')
    
    
    raw_notes = raw_text.split("|||END OF NOTE|||")

    notes = []

    for note_text in raw_notes:
        note_text = note_text.strip()
        if not note_text:
            continue
        
        lines = note_text.split("\n", 1)
        title = lines[0].strip()

        if len(lines) > 1:
            content = (title + "\n" + lines[1]).strip()
        else:
            content = title 

        notes.append({
            "title": title,
            "content" : content
        })

    with open(NOTES_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)
    

    print(f"SYNC ERFOLGREICH!")
    print(f"{len(notes)} Notizen wurden frisch in die Datenbank geschrieben.") 
    return "OK", 200

if __name__ == "__main__":
    print("Listening on port 5000")
    app.run(host='0.0.0.0', port=5000)