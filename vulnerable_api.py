from fastapi import FastAPI

app = FastAPI()

orders = {
    1: {"user": "alice", "item": "Laptop"},
    2: {"user": "bob", "item": "Phone"},
}

@app.get("/")
def home():
    return {"message": "Vulnerable IDOR API running"}

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    return orders.get(order_id)