### Run in development Mode
#### Linux and Mac
```
export FLASK_APP=api
export FLASK_ENV=development
flask run
```

#### Windows
```
set FLASK_APP=api
set FLASK_ENV=development
flask run
```

#### Windows Powershell
```
$env:FLASK_APP = "api"
$env:FLASK_ENV = "development"
flask run
```

## Test
`curl -i -X POST -F filedata=@assets/cat.jpg http://localhost:5000/predict`

### Example Output
```
HTTP/1.1 100 Continue

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 63
Server: Werkzeug/1.0.1 Python/3.9.1
Date: Wed, 03 Mar 2021 06:54:37 GMT

{
"class_id": "n02124075",
"class_name": "Egyptian_cat"
}
```
