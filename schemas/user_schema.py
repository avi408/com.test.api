USER_SCHEMA = {
    "type": "object",
    "required": [
        "id",
        "name",
        "username",
        "email"
    ],
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "username": {
            "type": "string"
        },
        "email": {
            "type": "string"
        }
    }
}