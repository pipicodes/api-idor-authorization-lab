# Attack Demonstration

## Project Summary
This lab demonstrates an Insecure Direct Object Reference (IDOR) / Broken Object Level Authorization (BOLA) issue in an API.

## Vulnerable Behavior
The vulnerable API allows a user to access order records directly by changing the order ID in the URL.

Examples:
- `/orders/1`
- `/orders/2`

Because no ownership validation is performed, a user can access another user's order.

## Security Risk
This exposes sensitive information belonging to other users and demonstrates broken authorization logic.

## Secure Behavior
The secure version validates that the requested resource belongs to the authenticated user before returning the order.

If the order does not belong to the user, the API returns:

- `403 Access denied`

## Key Lesson
APIs must enforce authorization checks on every object request. Authentication alone is not enough.