import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError


import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_subtract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(response.status, http.client.OK)
        value = int(response.read().decode('utf-8'))
        self.assertEqual(value, 0)
    
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/2/0"
        
        with self.assertRaises(Exception) as context:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.status, http.client.INTERNAL_SERVER_ERROR, f"Error en la petición API a {url}"
            )

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        value = int(response.read().decode('utf-8'))
        self.assertEqual(value, 4)
    
    def test_api_square_root(self):
        url = f"{BASE_URL}/calc/square_root/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK, f"Error en la petición API a {url}")
        value = float(response.read().decode('utf-8'))
        self.assertEqual(value, 2.0)

    def test_api_square_root_negative(self):
        url = f"{BASE_URL}/calc/square_root/-2"
        
        with self.assertRaises(Exception) as context:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertEqual(
                response.status, http.client.OK, f"Error en la petición API a {url}"
            )

    def test_test_api_log10_invalid_parameter(self):        
        url = f"{BASE_URL}/calc/log10/yy"
        
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, 400)

    def test_test_api_log10_negative_parameter(self):        
        url = f"{BASE_URL}/calc/log10/-100"
        
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, 400)
