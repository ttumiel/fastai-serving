from django.test import TestCase
from django.urls import reverse

class IndexViewTests(TestCase):
    def test_index(self):
        """
        test index loads
        """
        response = self.client.get(reverse('web:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Serving Pytorch Models")

    def test_index_post(self):
        """
        test posting an image
        """
        with open("web/tests/dog.jpg", "rb") as f:
            response = self.client.post(reverse('web:index'), data={"image": f}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your Result is")
