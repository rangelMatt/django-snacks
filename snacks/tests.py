from django.test import SimpleTestCase, TestCase
from django.urls import reverse

# Create your tests here.

class SnacksTests(SimpleTestCase):
  def test_home_page_status(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    
  def test_home_page_template(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'home.html')
    self.assertTemplateUsed(response, 'base.html')
    
  def test_about_page_template(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'about.html')
    
  def test_not_found(self):
    # url = reverse('unknown')
    url = 'unknown/'
    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)