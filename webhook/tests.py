from django.test import TestCase
from django.urls import reverse
from .config import TG_TOKEN
import json

class IndexViewTests(TestCase):
    def test_bot_message(self):
        """
        test post message to bot
        """
        with open("webhook/tests/message.json", "r") as f:
            response = self.client.post(reverse('webhook:predict',
                                                args=[TG_TOKEN]),
                                                data=json.loads(f.read()),
                                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), '{"Status": 1}')

    # def test_bot_predict(self):
    #     """
    #     test posting an image
    #     """
    #     with open("web/tests/dog.jpg", "rb") as f:
    #         response = self.client.post(reverse('web:index'), data={"image": f}, follow=True)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Your Result is")
