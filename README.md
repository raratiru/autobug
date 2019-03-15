# autobug

Django bug: https://code.djangoproject.com/ticket/30256#ticket

* `git clone https://github.com/raratiru/autobug`
* `cd autobug`
* `pip install -r requirements`
* Install django-debug-toolbar
* `./manage.py runserver`
* http://127.0.0.1:8000/admin/inl/master/1/change/
* username: admin, password: admin

In the above URL, [`Master`](https://github.com/raratiru/autobug/blob/master/inl/models.py#L18) has all its inlines activated with `autocomplete_fields`, the number of queries is **awesome**.

By commenting out `autocomplete_fields` in [`inl/admin.py`](https://github.com/raratiru/autobug/blob/master/inl/admin.py#L38) the number of queries returns to normal.

By enabling the `form` attribute in [`inl/admin.py`](https://github.com/raratiru/autobug/blob/master/inl/admin.py#L39), django-autocomplete-light gets activated without harming the minimal count of queries.
