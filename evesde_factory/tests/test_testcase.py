"""Tests for the public test case base classes."""

# Standard Library
import socket

# Django
from django.contrib.messages import get_messages
from django.test import RequestFactory

# AA EVE SDE Factory
from evesde_factory.allianceauth import UserFactory, UserMainFactory
from evesde_factory.testcase import (
    AuthTestCase,
    NoSocketsTestCase,
    SocketAccessError,
)


class TestNoSocketsTestCase(NoSocketsTestCase):
    """Test the network guard."""

    def test_should_raise_error_when_accessing_network(self):
        with self.assertRaises(SocketAccessError):
            socket.socket()

    def test_should_replace_socket_with_guard(self):
        self.assertIs(socket.socket, self.guard)
        self.assertIsNot(socket.socket, self.socket_original)


class TestAuthTestCase(AuthTestCase):
    """Test the default users and helpers."""

    def test_should_create_users_with_default_factory_class(self):
        self.assertIs(AuthTestCase.factory_class, UserFactory)
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.superuser.is_superuser)
        self.assertNotEqual(self.user.pk, self.superuser.pk)
        self.assertIsInstance(self.factory, RequestFactory)

    def test_should_set_session_and_messages(self):
        request = self.factory.get("/")
        self._middleware_process_request(request)
        self.assertTrue(hasattr(request, "session"))
        self.assertEqual(list(get_messages(request)), [])


class TestAuthTestCaseFactoryClass(AuthTestCase):
    """Test that a subclass builds its users with `factory_class`."""

    factory_class = UserMainFactory

    def test_should_create_users_with_custom_factory_class(self):
        self.assertTrue(self.user.profile.main_character)
        self.assertTrue(self.superuser.profile.main_character)
        self.assertTrue(self.superuser.is_superuser)
