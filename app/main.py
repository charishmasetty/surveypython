from fastapi import FastAPI
from . import models, database, routes

#models.Base.metadata.drop_all(bind=database.engine)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(routes.router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}

#@app.get("/")
#def read_root():
#    return {"message": "🚀 Pipeline deployment success!"}
