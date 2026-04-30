from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import engine
from backend.models import Base

from backend.database import SessionLocal
from backend.models import Entry

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#entries = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/entries")
def create_entry(entry: dict):
    db = SessionLocal()
    new_entry = Entry(
        date=entry.get("date"),
        title=entry.get("title"),
        category=entry.get("category"),
        did_it=entry.get("did_it"),
        notes=entry.get("notes")
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    db.close()
    return {"message": "Entry created successfully", "entry_id": new_entry.id}
# entries=[] 
# def create_entry(entry: dict):
    
#     entries.append(entry) 
#     return {"message": "Entry created successfully"}


@app.get("/entries")
def get_entries():
    db = SessionLocal()
    db_entries = db.query(Entry).all()
    result = []
    for entry in db_entries:    
        result.append({
            "id": entry.id,
            "date": entry.date,
            "title": entry.title,
            "category": entry.category,
            "did_it": entry.did_it,
            "notes": entry.notes
        })
    db.close()
    return {"entries": result}

    # return {"entries": entries}
# count = 0
# @app.get("/stats")
# def get_stats():
#     length = len(entries)
#     if "did_it"==True:
#         count += 1
#         if length>0:
#             completion_rate = (count/length)*100
#             return {"completion_rate": completion_rate}
#         else:
#             return{"message": "No entries to calculate completion rate"}
@app.delete("/entries/{id}")
def delete_entry(id: int):
    db = SessionLocal()
    entry = db.query(Entry).filter(Entry.id == id).first()

    if not entry:
        db.close()
        return {"message": "Entry not found"}

    db.delete(entry)
    db.commit()
    db.close()

    return {"message": "Entry deleted successfully"}

@app.put("/entries/{id}")
def update_entry(id: int, updated_entry: dict):
    db = SessionLocal()
    entry = db.query(Entry).filter(Entry.id == id).first()

    if not entry:
        db.close()
        return {"message": "Entry not found"}

    entry.date = updated_entry.get("date", entry.date)
    entry.title = updated_entry.get("title", entry.title)
    entry.category = updated_entry.get("category", entry.category)
    entry.did_it = updated_entry.get("did_it", entry.did_it)
    entry.notes = updated_entry.get("notes", entry.notes)

    db.commit()
    db.refresh(entry)
    db.close()

    return {"message": "Entry updated successfully"}

@app.get("/stats")
def get_stats():
    db = SessionLocal()
    db_entries = db.query(Entry).all()
    
    length = len(db_entries)
    count = 0
    # db.close()
    for i in db_entries:
        if i.did_it == True:
            count += 1
        # if i.get("did_it") == True:
        #     count += 1

    db.close() 
    if length > 0:
        completion_rate = (count / length) * 100
        
    
        return {"completion_rate": completion_rate, "total_entries": length, "completed_entries": count}
    else:
        return {"message": "No entries to calculate completion rate"}
