from django.test import TestCase


class ViewTests(TestCase):
    def test_home_returns_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content.decode(),
            "<h1>Hello, World!, This is the home page.</h1>",
        )
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")

    def test_about_returns_about_page(self):
        response = self.client.get("/about/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "<h1>This is the about page.</h1>")
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")

    def test_api_home_returns_status_payload(self):
        response = self.client.get("/api/status/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "message": "CI/CD pipeline is working successfully!",
                "status": "success",
                "version": "1.1",
            },
        )
        self.assertEqual(response["Content-Type"], "application/json")

    def test_api_home_rejects_non_get_requests(self):
        response = self.client.post("/api/status/")

        self.assertEqual(response.status_code, 405)
