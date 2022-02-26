# import pickle
# import os
# import sys
#
# from test_server import Response
#
# from tests.util import BaseGrabTestCase, temp_dir
# from grab import Grab
# from grab.error import GrabMisuseError
#
# FAKE_TRANSPORT_CODE = """
# from grab.transport.DEPRECATED import DEPRECATEDTransport
#
# class FakeTransport(DEPRECATEDTransport):
#    pass
# """
#
#
# def get_fake_transport_class():
#    from grab.transport.DEPRECATED import (  # pylint: disable=import-outside-toplevel
#        DEPRECATEDTransport,
#    )
#
#    class FakeTransport(DEPRECATEDTransport):
#        pass
#
#    return FakeTransport
#
#
# def get_fake_transport_instance():
#    return get_fake_transport_class()()
#
#
# def get_DEPRECATED_transport_instance():
#    from grab.transport.DEPRECATED import (  # pylint: disable=import-outside-toplevel
#        DEPRECATEDTransport,
#    )
#
#    return DEPRECATEDTransport()
#
#
# class TestTransportTestCase(BaseGrabTestCase):
#    def assert_transport_response(self, transport, response):
#        self.server.add_response(Response(data=response), count=2)
#
#        grab = Grab(transport=transport)
#        grab.go(self.server.get_url())
#        self.assertEqual(grab.doc.body, response)
#
#        grab2 = grab.clone()
#        grab2.go(self.server.get_url())
#        self.assertEqual(grab2.doc.body, response)
#
#    def assert_transport_pickle(self, transport, response):
#        grab = Grab(transport=transport)
#        grab2 = grab.clone()
#        grab2_data = pickle.dumps(grab2, pickle.HIGHEST_PROTOCOL)
#        grab3 = pickle.loads(grab2_data)
#        grab3.go(self.server.get_url())
#        self.assertEqual(grab3.doc.body, response)
#
#    # def test_transport_option_as_string_DEPRECATED(self):
#    #    self.assert_transport_response("grab.transport.DEPRECATED.DEPRECATEDTransport", b"XYZ")
#
#    # def test_transport_option_as_string_fake(self):
#    #    with temp_dir() as dir_:
#    #        sys.path.insert(0, dir_)
#    #        with open(os.path.join(dir_, "foo.py"), "w", encoding="utf-8") as out:
#    #            out.write(FAKE_TRANSPORT_CODE)
#    #        self.assert_transport_response("foo.FakeTransport", b"XYZ")
#    #        sys.path.remove(dir_)
#
#    # def test_transport_option_as_class_DEPRECATED(self):
#    #    from grab.transport.DEPRECATED import (  # pylint: disable=import-outside-toplevel
#    #        DEPRECATEDTransport,
#    #    )
#
#    #    self.assert_transport_response(DEPRECATEDTransport, b"XYZ")
#
#    # def test_transport_option_as_class_fake(self):
#    #    fake_transport_cls = get_fake_transport_class()
#    #    self.assert_transport_response(fake_transport_cls, b"XYZ")
#
#    # def test_transport_option_as_function_DEPRECATED(self):
#    #    self.assert_transport_response(get_DEPRECATED_transport_instance, b"XYZ")
#
#    # def test_transport_option_as_function_fake(self):
#    #    self.assert_transport_response(get_fake_transport_instance, b"XYZ")
#
#    def test_invalid_transport_invalid_alias(self):
#        with self.assertRaises(GrabMisuseError):
#            Grab(transport="zzzzzzzzzz").go(self.server.get_url())
#
#    def test_invalid_transport_invalid_path(self):
#        # AttributeError comes from setup_transport method
#        with self.assertRaises(AttributeError):
#            Grab(transport="tests.grab_transport.DEPRECATED").go(self.server.get_url())
#
#    def test_invalid_transport_not_collable_or_string(self):
#        with self.assertRaises(GrabMisuseError):
#            Grab(transport=13).go(self.server.get_url())
#
#    def test_setup_transport_twice(self):
#        transport = "grab.transport.DEPRECATED.DEPRECATEDTransport"
#        grab = Grab()
#        grab.setup_transport(transport)
#        with self.assertRaises(GrabMisuseError) as ex:
#            grab.setup_transport(transport)
#        self.assertTrue("Transport is already set up" in str(ex.exception))
#
#    def test_setup_transport_none(self):
#        grab = Grab()
#        self.assertTrue(grab.transport is None)
#
#        grab.setup_transport(None)
#        self.assertEqual(grab.transport_param, "grab.transport.DEPRECATED.DEPRECATEDTransport")
#
#    def test_setup_transport_callable(self):
#        from grab.transport.DEPRECATED import (  # pylint: disable=import-outside-toplevel
#            DEPRECATEDTransport,
#        )
#
#        grab = Grab()
#        grab.setup_transport(DEPRECATEDTransport)
#        self.assertTrue(isinstance(grab.transport, DEPRECATEDTransport))
