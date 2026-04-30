from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

entries = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/entries")
# entries=[] 
def create_entry(entry: dict):
    
    entries.append(entry) 
    return {"message": "Entry created successfully"}

@app.get("/entries")
def get_entries():
    return {"entries": entries}
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
@app.get("/stats")
def get_stats():
    length = len(entries)
    count = 0
    for i in entries:
        if i.get("did_it") == True:
            count += 1
    if length > 0:
        completion_rate = (count / length) * 100
        return {"completion_rate": completion_rate, "total_entries": length, "completed_entries": count}
    else:
        return {"message": "No entries to calculate completion rate"}
