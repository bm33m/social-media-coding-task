# social-media-coding-task
social-media-coding-task

```
$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

test01:
visit:
http://127.0.0.1:5000/testapi


```


test02:
```
 """
  Using async and await
  Changelog

  Routes, error handlers, before request, after request,
  and teardown functions can all be coroutine functions
  if Flask is installed with the async extra (pip install flask[async]).
  This allows views to be defined with async def and use await.

  @app.route("/get-data")
  async def get_data():
      data = await async_db_query(...)
      return jsonify(data)
  """
test02:
visit:
http://127.0.0.1:5000/

```


Using async on Windows on Python 3.8

  Python 3.8 has a bug related to asyncio on Windows.
  If you encounter something like ValueError: set_wakeup_fd only works in main thread,
  please upgrade to Python 3.9.


```
$ py app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ***-***-***
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)

visit01:
http://127.0.0.1:8000/testapi

visit02:
http://127.0.0.1:8000/


Enjoy....

```
