# 🏪 Flask Store & Item REST API

A simple and extendable RESTful API for managing stores and their items — built with **Python Flask**.
This project follows clean backend architecture with proper routing, validation, and OpenAPI documentation via **Flask-Smorest**.

---

## 📝 Features

* Full CRUD for Stores
* Full CRUD for Items
* Each store includes:

  * `name` (required)
  * `id` (UUID)
* Each item includes:

  * `name` (required)
  * `price` (required, float)
  * `store_id` (must exist)
  * `id` (UUID)
* Input validation using Marshmallow
* RESTful structure using Blueprints and MethodView
* OpenAPI documentation via Flask-Smorest
* Docker support
* JWT-based authentication 

---

## 🚧 Project Progress Checklist

| Day | Feature                                | Status    |
| --- | -------------------------------------- | --------- |
| 1   | Basic Flask App with GET, POST, DELETE | ✅ Done    |
| 2   | Add PUT for updating items             | ✅ Done    |
| 3   | Add input validation via Marshmallow   | ✅ Done    |
| 4   | Refactor with Blueprints               | ✅ Done    |
| 5   | Use MethodView Class-Based Views       | ✅ Done    |
| 6   | Add Flask-Smorest with Swagger UI      | ✅ Done    |
| 7   | Add Docker Containerization            | ✅ Done    |
| 8   | Database Integration with SQLAlchemy   | ⬜ Pending |
| 9   | Add JWT Authentication                 | ⬜ Pending |

---

## 📘 API Endpoints

### 🔹 `GET /store`

**Description:** Retrieve all stores.

**Responses:**

* `200 OK`: Returns a list of stores.

---

### 🔹 `POST /store`

**Description:** Create a new store.

**Request Body (JSON):**

```json
{
  "name": "My New Store"
}
```

**Responses:**

* `201 Created`: Returns the created store.
* `400 Bad Request`: If the store already exists.

---

### 🔹 `GET /store/<store_id>`

**Description:** Retrieve a single store by its ID.

**Responses:**

* `200 OK`: Returns the store.
* `404 Not Found`: If the store does not exist.

---

### 🔹 `DELETE /store/<store_id>`

**Description:** Delete a store by its ID.

**Responses:**

* `200 OK`: Confirmation message.
* `404 Not Found`: If the store does not exist.

---

### 🔸 `GET /item`

**Description:** Retrieve all items.

**Responses:**

* `200 OK`: Returns a list of items.

---

### 🔸 `POST /item`

**Description:** Create a new item in a store.

**Request Body (JSON):**

```json
{
  "name": "Apple",
  "price": 0.99,
  "store_id": "your_store_id_here"
}
```

**Responses:**

* `201 Created`: Returns the created item.
* `400 Bad Request`: If item already exists.
* `404 Not Found`: If the `store_id` does not exist.

---

### 🔸 `GET /item/<item_id>`

**Description:** Retrieve a single item by its ID.

**Responses:**

* `200 OK`: Returns the item.
* `404 Not Found`: If the item does not exist.

---

### 🔸 `PUT /item/<item_id>`

**Description:** Update an existing item.

**Request Body (JSON):**

```json
{
  "name": "Green Apple",
  "price": 1.25
}
```

**Responses:**

* `200 OK`: Returns the updated item.
* `404 Not Found`: If the item does not exist.

---

### 🔸 `DELETE /item/<item_id>`

**Description:** Delete an item by its ID.

**Responses:**

* `200 OK`: Confirmation message.
* `404 Not Found`: If the item does not exist.

---

# 🔧 Local Installation

## 📦 Using Python (venv)

### Create virtual environment & activate

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app

```bash
flask run
```

---

## 🐳 Using Docker

### Build Docker image

```bash
docker build -t flask-store-item-api .
```

### Run container

```bash
docker run -p 5000:5000 flask-store-item-api
```

### Run multiple containers using docker-compose

```bash
docker-compose up --build
```

---

Let me know if you want this in a downloadable `README.md` file or want to add authentication/database next.
