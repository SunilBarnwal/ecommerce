# from django.contrib.auth import get_user_model
from django.test import TestCase
# from django.urls import reverse

# from .models import Products


# class ProductDetailViewTests(TestCase):
#     def test_product_detail_page_loads_for_selected_product(self):
#         user = get_user_model().objects.create_user(username='tester', email='tester@example.com', password='secret123')
#         product = Products.objects.create(
#             name='Wireless Headphones',
#             price=1999.00,
#             qty=5,
#             desc='Noise cancelling headphones with 40h battery.',
#             created_by=user,
#         )

#         self.client.force_login(user)
#         response = self.client.get(reverse('view_details', args=[product.id]))

#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Wireless Headphones')
