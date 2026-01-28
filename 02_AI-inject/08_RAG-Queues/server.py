from client.rq_clients import queue
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
def root():
    return {"Status": "Server is up and running"}


@app.get("/post")
def chat(query: str = Query(..., description="The input query for the chat model")):
    job = queue.enqueue("queues.worker.process_query", query)
    return {"Job_ID": job.id, "Status": "Queued"}


@app.get("/status")
def get_result(job_id: str = Query(..., description="Job ID fetch result")):
    job = queue.fetch_job(job_id)

    if job is None:
        return {"Status": "Job not found", "Result": None}

    if job.is_finished:
        return {"Status": "Completed", "Result": job.result}
    elif job.is_failed:
        return {"Status": "Failed", "Error": str(job.exc_info)}
    else:
        return {"Status": job.get_status(), "Result": None}