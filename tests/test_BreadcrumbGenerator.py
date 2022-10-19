from unittest import TestCase

from BreadcrumbGenerator import generate_bc


class Test(TestCase):
    def test_colon(self):
        test, ans = [
            ("mysite.com/pictures/holidays.html", " : "),
            '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
        ]
        self.assertEqual(ans, generate_bc(**test))

    def test_forward_slash(self):
        test, ans = [
            ("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / "),
            '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
        ]
        self.assertEqual(ans, generate_bc(**test))

    def test_star(self):
        test, ans = [
            ("www.microsoft.com/important/confidential/docs/index.htm#top", " * "),
            '<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * <a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>'
        ]
        self.assertEqual(ans, generate_bc(**test))

    def test_greater_than(self):
        test, ans = [
            ("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > "),
            '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
        ]
        self.assertEqual(ans, generate_bc(**test))

    def test_plus(self):
        test, ans = [
            ("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + "),
            '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'
        ]
        self.assertEqual(ans, generate_bc(**test))
