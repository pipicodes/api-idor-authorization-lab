# API IDOR Authorization Lab

This project demonstrates a Broken Object Level Authorization (IDOR/BOLA) vulnerability and how proper authorization checks prevent it.

---

## Vulnerable API

Run:

```bash
python3 -m uvicorn vulnerable_api:app --reload

The vulnerable API allows access to any order ID without validating ownership.
```

## Secure API
```bash
python3 -m uvicorn secure_api:app --reload --port 8001

The secure API validates that the authenticated user owns the requested resource.
```

