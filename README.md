## Flask API Manager

Protect your API with WWW-authenticate AND with allowed method(s) per API consumer.

Supported methods:

* GET
* POST
* PUT
* DELETE

### Demo?

1. Git clone <link>
2. _cd_ directory
3. Run ``sudo pip3 install -r requirements.txt``
4. Open Python3 / Ipython3
    ```
    from exampe import db
    db.create_all()
    ```
5. Run ``python3 example.py``

Note: It will use the app.db SQLite file, located in the Git repository.

#### Results:
##### GET Method
```
curl http://127.0.0.1:5000/ -u "test:a78297072831af169e308a655254aa2f2264567453b13101ee2891bd199bb06f" -X GET
{
  "Message": "Hello World!"
}
```

##### POST Method
```
curl http://127.0.0.1:5000/ -u "test:a78297072831af169e308a655254aa2f2264567453b13101ee2891bd199bb06f" -X GET
{
  "Message": "Hello World!"
}
```

##### PUT Method
```
curl http://127.0.0.1:5000/ -u "test:a78297072831af169e308a655254aa2f2264567453b13101ee2891bd199bb06f" -X GET
{
  "Message": "Hello World!"
}
```

##### DELETE Method
```
curl http://127.0.0.1:5000/ -u "test:a78297072831af169e308a655254aa2f2264567453b13101ee2891bd199bb06f" -X GET
{
  "Message": "Not authorized."
}
```

### Requirements

Flask-API-Management used Flask_restful. See requirements.txt for more details.