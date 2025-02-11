from grab import Grab
from tests.util import BaseGrabTestCase

HTML = """
<head>
    <title>фыва</title>
    <meta http-equiv="Content-Type" content="text/html; charset=cp1251" />
</head>
<body>
    <div id="bee">
        <div class="wrapper">
            <strong id="bee-strong">пче</strong><em id="bee-em">ла</em>
        </div>
        <script type="text/javascript">
        mozilla = 777;
        </script>
        <style type="text/css">
        body { color: green; }
        </style>
    </div>
    <div id="fly">
        <strong id="fly-strong">му\n</strong><em id="fly-em">ха</em>
    </div>
    <ul id="num">
        <li id="num-1">item #100 2</li>
        <li id="num-2">item #2</li>
    </ul>
""".encode(
    "cp1251"
)


class PyqueryExtensionTest(BaseGrabTestCase):
    def setUp(self):
        # Create fake grab instance with fake response
        self.grab = Grab(HTML, charset="cp1251")

    def test_some_things(self):
        # pytype: disable=import-error
        from pyquery import PyQuery  # pylint: disable=import-outside-toplevel

        # pytype: enable=import-error

        self.assertEqual(self.grab.doc.pyquery("#num-1").text(), "item #100 2")
        self.assertEqual(
            self.grab.doc.pyquery("li")
            .filter(lambda x: "#2" in PyQuery(x).text())
            .text(),
            "item #2",
        )
