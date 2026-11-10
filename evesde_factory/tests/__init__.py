# AA EVE SDE Factory
from evesde_factory.allianceauth import UserMainFactory
from evesde_factory.testcase import AuthTestCase as BaseAuthTestCase
from evesde_factory.testcase import NoSocketsTestCase, SocketAccessError

__all__ = ["AuthTestCase", "NoSocketsTestCase", "SocketAccessError"]


class AuthTestCase(BaseAuthTestCase):
    """Testcase with users created by the `UserMainFactory`."""

    factory_class = UserMainFactory
