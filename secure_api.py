from fastapi import FastAPI, HTTPException

app = FastAPI()

orders = {
    1: {"user": "alice", "item": "Laptop"},
    2: {"user": "bob", "item": "Phone"},
    3: {"user": "charlie", "item": "Tablet"}
}

# Simulated logged-in user
current_user = "alice"

@app.get("/")
def home():
    return {"message": "Secure API running"}

@app.get("/orders/{order_id}")
def get_order(order_id: int):

    order = orders.get(order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order["user"] != current_user:
        raise HTTPException(status_code=403, detail="Access denied")

    return order