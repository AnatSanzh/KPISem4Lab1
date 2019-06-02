from flask import Flask


class TestApi:
    """docstring for TestApi"""

    def test_add_record(self, app: Flask):
        client = app.test_client()
        req = client.post('/records', data={
                'number': "+380",
                'name': "the_name",
                "address": "address"
            })
        assert req.status_code == 200

    def test_get_record(self, app: Flask):
        client = app.test_client()
        req = client.get('/record/+380')
        assert req.status_code == 200

    def test_update_record(self, app: Flask):
        client = app.test_client()
        req = client.put('/record/+380', data={
            'name': "ddf",
            'address': "sfds"
        })
        assert req.status_code == 200

    def test_remove_record(self, app: Flask):
        client = app.test_client()
        req = client.delete('/record/+380')
        assert req.status_code == 200

    def test_clear_records(self, app: Flask):
        client = app.test_client()
        req = client.delete('/records')
        assert req.status_code == 200

    def test_get_list_records(self, app: Flask):
        client = app.test_client()
        req = client.get('/records', data={
            'offset': 1,
            'count': 2
        })
        assert req.status_code == 200
