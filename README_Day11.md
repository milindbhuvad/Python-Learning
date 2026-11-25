# Python Learning -- Day 11: Validation, Error Handling and JWT Authentication Basics

## Learning objectives

-   Pydantic request validation
-   HTTP status codes and error handling
-   Password hashing with Argon2
-   JWT access-token creation and verification
-   Protected API endpoints

## 1. Pydantic validation

Update `schemas.py`:

``` python
from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


class ProductResponse(ProductCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
```

Validation rules: - `min_length=2`: product name must contain at least
two characters. - `max_length=150`: product name can contain at most 150
characters. - `gt=0`: price must be greater than zero. - `ge=0`:
quantity must be zero or greater.

Try this invalid request in Swagger:

``` json
{
  "name": "A",
  "price": -100,
  "quantity": -5
}
```

FastAPI should return **422 Unprocessable Entity** because the request
data does not satisfy the schema.

## 2. Error handling and HTTP status codes

FastAPI uses `HTTPException` to return HTTP errors:

``` python
from fastapi import HTTPException

if product is None:
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
```

  Code   Meaning
  ------ -----------------------
  200    OK
  201    Created
  400    Bad Request
  401    Unauthorized
  403    Forbidden
  404    Not Found
  422    Validation Error
  500    Internal Server Error

-   **401**: authentication is missing or invalid.
-   **403**: the user is authenticated but not allowed to access the
    resource.
-   **404**: the requested resource does not exist.
-   **422**: request data failed validation.

## 3. Install authentication packages

Activate your virtual environment, then run:

``` powershell
cd D:\Python-Learning
.\.venv\Scripts\Activate.ps1

python -m pip install "pwdlib[argon2]" PyJWT
```

-   `pwdlib[argon2]`: securely hashes and verifies passwords.
-   `PyJWT`: creates and verifies JSON Web Tokens.

## 4. Password hashing

Never store a user's plain-text password in a database. Store a password
hash instead.

Laravel:

``` php
Hash::make($password);
Hash::check($password, $hashedPassword);
```

Python:

``` python
password_hash.hash(password)
password_hash.verify(password, hashed_password)
```

Password hashing is one-way: the application verifies a submitted
password against the stored hash rather than decrypting the hash.

## 5. Create `auth.py`

For this learning exercise, authentication uses one demonstration user
stored in memory. This is **not production-ready**; a real application
should retrieve users from MySQL and store password hashes in the users
table.

``` python
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

router = APIRouter()
password_hash = PasswordHash.recommended()
security = HTTPBearer()

# Replace with a strong secret stored in an environment variable.
# Never commit a real secret to Git.
SECRET_KEY = "REPLACE_WITH_YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Demo user only. A real application should load this from MySQL.
demo_user = {
    "email": "admin@example.com",
    "hashed_password": password_hash.hash("Admin@123")
}


class LoginRequest(BaseModel):
    email: str
    password: str


def create_access_token(email: str):
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": email,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


@router.post("/login")
def login(user: LoginRequest):

    if user.email != demo_user["email"]:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not password_hash.verify(
        user.password,
        demo_user["hashed_password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(user.email)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        if email != demo_user["email"]:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return email

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


@router.get("/profile")
def profile(current_user: str = Depends(get_current_user)):

    return {
        "message": "Authentication successful",
        "email": current_user
    }
```

### Generate a strong secret key

Run:

``` powershell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Use the generated value for local practice. For better security, load it
from an environment variable instead of hardcoding it. Never commit it
to GitHub.

## 6. Connect authentication to FastAPI

In `main.py`, add:

``` python
from auth import router as auth_router

app.include_router(auth_router)
```

Place `app.include_router(auth_router)` after `app = FastAPI(...)`. Keep
your existing product CRUD routes.

## 7. Test authentication in Swagger

Start the application:

``` powershell
fastapi dev main.py
```

Open <http://127.0.0.1:8000/docs>.

### Step 1: Login

Call `POST /login` with:

``` json
{
  "email": "admin@example.com",
  "password": "Admin@123"
}
```

Expected response:

``` json
{
  "access_token": "YOUR_GENERATED_TOKEN",
  "token_type": "bearer"
}
```

### Step 2: Authorize

1.  Copy the `access_token` value.
2.  Click **Authorize** in Swagger.
3.  Enter the token in the Bearer authentication field.
4.  Confirm authorization.

### Step 3: Test the protected endpoint

Call `GET /profile`.

Expected response:

``` json
{
  "message": "Authentication successful",
  "email": "admin@example.com"
}
```

Try calling `/profile` without a token. The request should be rejected.

## 8. Laravel vs FastAPI comparison

  Laravel                   Python FastAPI
  ------------------------- --------------------------
  `Hash::make()`            `password_hash.hash()`
  `Hash::check()`           `password_hash.verify()`
  Sanctum / Passport        JWT with PyJWT
  Middleware                Dependency injection
  `abort(404)`              `HTTPException(404)`
  Form Request validation   Pydantic validation

## 9. Day 11 practical checklist

-   [ ] Add Pydantic validation to `ProductCreate`.
-   [ ] Test invalid product data in Swagger.
-   [ ] Understand common HTTP status codes.
-   [ ] Install `pwdlib[argon2]` and `PyJWT`.
-   [ ] Create `auth.py`.
-   [ ] Generate a strong JWT secret key.
-   [ ] Test the login API.
-   [ ] Test the protected profile API.
-   [ ] Test missing, invalid, and expired tokens.

## 10. Production notes

This is a learning implementation, not a complete production
authentication system.

Before using a similar design in a real application:

-   Store users and password hashes in MySQL.
-   Load the JWT secret from a secure environment variable or secrets
    manager.
-   Use HTTPS.
-   Add registration, logout/token revocation or refresh-token handling
    as appropriate.
-   Apply authorization checks and rate limits.
-   Do not expose passwords, hashes, or secrets in API responses or
    logs.
-   Consider FastAPI's OAuth2 password-bearer flow for a more standard
    OAuth2-style implementation.

## 11. What's next?

**Day 12 -- Dockerize FastAPI + MySQL**

Topics: - Dockerfile for FastAPI - Docker Compose - FastAPI container -
MySQL container - Environment variables - Run the complete application
using Docker

------------------------------------------------------------------------

**Day 11 completed:** Validation, error handling, password hashing, JWT
basics, and protected API endpoints.
