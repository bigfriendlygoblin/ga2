from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from mangum import Mangum

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

students_data = [
    {"name":"fgIxp","marks":33},{"name":"8uAyS7pT","marks":2},{"name":"A3","marks":87},
    {"name":"6T1woCR","marks":65},{"name":"hW1Y","marks":5},{"name":"o","marks":43},
    {"name":"rdX5Fqsf8","marks":29},{"name":"P","marks":25},{"name":"s5W5Y","marks":33},
    {"name":"DYGF","marks":35},{"name":"Nx0U1H6W","marks":73},{"name":"MkjL7xo06","marks":36},
    {"name":"nNLJz","marks":64},{"name":"sk0mJwQ","marks":59},{"name":"BcclGe","marks":39},
    {"name":"5x","marks":7},{"name":"2ZBxbFIYEC","marks":29},{"name":"E8wbP3qA","marks":34},
    {"name":"v5","marks":11},{"name":"4dB","marks":49},{"name":"Ru0DEL","marks":5},
    {"name":"kqwocg9iSM","marks":27},{"name":"BTVcFy950b","marks":6},{"name":"v3vqWh6","marks":99},
    {"name":"mO","marks":63},{"name":"2HH","marks":19},{"name":"jW7","marks":62},
    {"name":"BzS","marks":34},{"name":"XwSAxv3e","marks":35},{"name":"WTqu","marks":11},
    {"name":"T","marks":83},{"name":"JOZr1PN814","marks":50},{"name":"9Srti4","marks":98},
    {"name":"3xfQ0Hm0Wm","marks":42},{"name":"x","marks":57},{"name":"Pi1uXXWDQ","marks":72},
    {"name":"ddYivH0M","marks":31},{"name":"MW","marks":48},{"name":"T0fq865Aue","marks":38},
    {"name":"2xWG","marks":16},{"name":"UEAC","marks":9},{"name":"u0Nm4","marks":77},
    {"name":"x1g","marks":98},{"name":"GgrdenYXry","marks":53},{"name":"Q4","marks":81},
    {"name":"UFPC","marks":33},{"name":"kFjCWNE","marks":82},{"name":"3","marks":82},
    {"name":"JzE","marks":85},{"name":"dFG6dX","marks":2},{"name":"8LT","marks":31},
    {"name":"PeYx","marks":24},{"name":"eittfx","marks":32},{"name":"HtkZkQtK9o","marks":69},
    {"name":"Zsj0","marks":23},{"name":"CzQ","marks":17},{"name":"Xi","marks":67},
    {"name":"qimEA","marks":50},{"name":"ZCO","marks":0},{"name":"C","marks":29},
    {"name":"S","marks":18},{"name":"7","marks":96},{"name":"vSKJYP4Xt0","marks":41},
    {"name":"3coJPf4","marks":92},{"name":"69yXq","marks":71},{"name":"YIKhYK7","marks":11},
    {"name":"n8Lxb0n5Jv","marks":89},{"name":"krb2c","marks":32},{"name":"6nJsQwc","marks":78},
    {"name":"hjal","marks":59},{"name":"0","marks":93},{"name":"wFK","marks":55},
    {"name":"0ZcCP","marks":32},{"name":"CXSY0","marks":93},{"name":"MQpuIftCVK","marks":70},
    {"name":"RtRYP1In","marks":40},{"name":"4lJVoRap","marks":43},{"name":"xGABbkJvQO","marks":91},
    {"name":"B","marks":49},{"name":"TkaVtut","marks":2},{"name":"Gsn","marks":71},
    {"name":"h0V","marks":76},{"name":"7neTOA6BV","marks":72},{"name":"VS2Jc","marks":46},
    {"name":"MSubQPL","marks":41},{"name":"00DBY","marks":20},{"name":"A8EvcQ","marks":30},
    {"name":"vAqoStwA","marks":76},{"name":"tyP2","marks":11},{"name":"2nWc","marks":65},
    {"name":"tSn","marks":83},{"name":"vD8LCRRQa","marks":9},{"name":"sqRYFfLX","marks":7},
    {"name":"qGf","marks":80},{"name":"Lpx0qIw3M","marks":51},{"name":"eD","marks":25},
    {"name":"oiqmYReBp6","marks":89},{"name":"zJV41DWth","marks":7},{"name":"aWI3x7","marks":16},
    {"name":"B4SdfoI0L","marks":34},
]

students_marks = {student['name']: student['marks'] for student in students_data}


@app.get("/api")
async def get_marks(name: Optional[List[str]] = Query(default=None)):
    if not name:
        # Return all data or a friendly message
        return {"message": "No names provided", "all_students_count": len(students_data)}
    result = [students_marks.get(n, None) for n in name]
    return {"marks": result}

handler = Mangum(app)
