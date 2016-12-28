# coding=utf-8

from ...helpers import LoggedInApplicationTest


class TestApplication(LoggedInApplicationTest):
    def test_main_index(self):
        response = self.client.get('/admin')
        assert response.status_code == 200

    def test_404(self):
        with self.app.app_context():
            response = self.client.get('/admin/not-found')
            assert response.status_code == 404

    def test_index_is_404(self):
        response = self.client.get('/')
        assert response.status_code == 404

    def test_headers(self):
        res = self.client.get('/admin')
        assert res.status_code == 200
        self.assertIn('Secure;', res.headers['Set-Cookie'])
        self.assertIn('DENY', res.headers['X-Frame-Options'])

    def test_response_headers(self):
        response = self.client.get('/admin')

        assert (
            response.headers['cache-control'] ==
            "no-cache"
        )
