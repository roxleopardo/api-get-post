# api-get-post

A simple Python API that accepts **GET** and **POST** requests with a JSON body and returns the same payload it received.

---

## Requirements

- Python 3.10+

---

## Setup

```bash
# 1. Create and activate the virtual environment
python -m venv .venv
# source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate         # Windows

# 2. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Running the API

```bash
python app.py
```

The server starts at `http://127.0.0.1:5000` by default.

---

## Endpoint

### `GET /echo` and `POST /echo`

Receives a JSON body and returns exactly the same content.

**Required headers**

| Header       | Value            |
|--------------|------------------|
| Content-Type | application/json |

**POST request example**

```bash
curl -X POST http://127.0.0.1:5000/echo \
     -H "Content-Type: application/json" \
     -d '{"name": "John", "age": 30}'
```

**Response (`200 OK`)**

```json
{
  "name": "John",
  "age": 30
}
```

**GET request example**

```bash
curl -X GET http://127.0.0.1:5000/echo \
     -H "Content-Type: application/json" \
     -d '{"filter": "active", "page": 1}'
```

**Response (`200 OK`)**

```json
{
  "filter": "active",
  "page": 1
}
```

---

## Error responses

| Scenario                                        | Status | Body                                           |
|-------------------------------------------------|--------|------------------------------------------------|
| Missing body or invalid JSON                    | `400`  | `{"error": "Request body must be valid JSON"}` |
| `Content-Type` other than `application/json`    | `400`  | `{"error": "Request body must be valid JSON"}` |

---

## Running the tests

```bash
# With the venv activated:
pytest -v
```

Expected output:

```
test_app.py::test_post_returns_same_json              PASSED
test_app.py::test_post_nested_json                    PASSED
test_app.py::test_post_empty_object                   PASSED
test_app.py::test_post_array                          PASSED
test_app.py::test_post_missing_body_returns_400       PASSED
test_app.py::test_post_invalid_json_returns_400       PASSED
test_app.py::test_post_wrong_content_type_returns_400 PASSED
test_app.py::test_get_returns_same_json               PASSED
test_app.py::test_get_missing_body_returns_400        PASSED
test_app.py::test_get_invalid_json_returns_400        PASSED
test_app.py::test_response_content_type_is_json       PASSED
```

---

## Project structure

```
api-get-post/
├── app.py            # Flask API
├── test_app.py       # pytest tests
├── requirements.txt  # Dependencies
└── README.md         # This documentation
```
