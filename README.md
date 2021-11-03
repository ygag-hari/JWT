## Django rest framework with JWT auth endpoints.

- Register users
- Login and obtain Access token and refresh token
- List users in the platform (endpoint with throttling 2 requests/15 minutes)
- Verify Users with OTP send via email


### Postman collection
```JSON
{
	"info": {
		"_postman_id": "052a4c8f-730f-44f3-9c41-5e0036e9a650",
		"name": "JWT",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "Get tokens",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"email\": \"mini@ygag.com\",\n    \"password\": \"password\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:8000/api/token/",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"api",
						"token",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "List users",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1OTE4NzA3LCJpYXQiOjE2MzU5MTg0MDcsImp0aSI6ImMyYjljNTExNzdjNjQ2Mjk4YTc3MjkxNjBjZGQ2ZWQ5IiwidXNlcl9pZCI6NH0.lAPwtspdCtt_zXv-UBxNe5bcB_L9XA42TBJRqmeE6KM",
							"type": "string"
						}
					]
				},
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:8000/core/users",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"core",
						"users"
					]
				}
			},
			"response": []
		},
		{
			"name": "Register",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"user\": { \n    \"email\": \"mini@ygag.com\",\n    \"username\": \"mini\",\n    \"password\": \"password\"\n  }\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:8000/core/register/",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"core",
						"register",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "verify user",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1OTE0NjU5LCJpYXQiOjE2MzU5MTQzNTksImp0aSI6ImRkYzE2MDYzZmU2MjQ5YWE5YmRmMTNjMzFiOTE2NGNhIiwidXNlcl9pZCI6NH0.Iet_upIFxJAA39RTO7RauzjcHXixxNLZqoELgu6B388",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"otp\": 2436\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:8000/core/verify/",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"core",
						"verify",
						""
					]
				}
			},
			"response": []
		}
	]
}
```
