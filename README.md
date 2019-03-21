# autobug

Django bug: https://code.djangoproject.com/ticket/30256#ticket

This bug is reproduced in
`PostgreSQL 9.6.11 on x86_64-pc-linux-gnu, compiled by gcc (Debian 6.3.0-18+deb9u1) 6.3.0 20170516, 64-bit.`

Debug toolbar is installed.
The files `queries*.txt`` include the queries report for each occasion, as reported from debug toolbar, for the url:

http://127.0.0.1:8000/admin/inl/child3/1/change/

The url http://127.0.0.1:8000/admin/inl/master/1/change/ includes all inlines which produce many more queries.

* `git clone https://github.com/raratiru/autobug`
* `cd autobug`
* `pip install -r requirements`
* Create the postgresql database
* ./manage.py migrate
* ./manage.py loaddata db.json
* `./manage.py runserver`
* http://127.0.0.1:8000/admin/inl/master/1/change/
* username: admin, password: admin

In the above URL, [`Master`](https://github.com/raratiru/autobug/blob/master/inl/models.py#L18) has all its inlines activated with `autocomplete_fields`, the number of queries is **awesome**.

By commenting out `autocomplete_fields` in [`inl/admin.py`](https://github.com/raratiru/autobug/blob/master/inl/admin.py#L38) the number of queries returns to normal.

By enabling the `form` attribute in [`inl/admin.py`](https://github.com/raratiru/autobug/blob/master/inl/admin.py#L39), django-autocomplete-light gets activated without harming the minimal count of queries.
