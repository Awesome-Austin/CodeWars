from unittest import TestCase

from BreadcrumbGenerator import generate_bc


class Test(TestCase):
    def test_colon(self):
        # noinspection SpellCheckingInspection
        test, ans = [
            ("mysite.com/pictures/holidays.html", " : "),
            '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
        ]
        self.assertEqual(ans, generate_bc(*test))

    def test_forward_slash(self):
        # noinspection SpellCheckingInspection
        test, ans = [
            ("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / "),
            '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
        ]
        self.assertEqual(ans, generate_bc(*test))

    def test_star(self):
        test, ans = [
            ("www.microsoft.com/important/confidential/docs/index.htm#top", " * "),
            '<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * '
            '<a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>'
        ]
        self.assertEqual(ans, generate_bc(*test))

    def test_greater_than(self):
        # noinspection SpellCheckingInspection
        test, ans = [
            ("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > "),
            '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > '
            '<span class="active">EXAMPLE</span>'
        ]
        self.assertEqual(ans, generate_bc(*test))

    def test_plus(self):
        # noinspection SpellCheckingInspection
        test, ans = [
            ("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + "),
            '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'
        ]
        self.assertEqual(ans, generate_bc(*test))

    def test_on_home_page_1(self):
        # noinspection SpellCheckingInspection
        test = ('www.agcpartners.co.uk/', '*')
        ans = '<span class="active">HOME</span>'
        self.assertEqual(ans, generate_bc(*test))

    def test_on_home_page_2(self):
        # noinspection SpellCheckingInspection
        test = ('www.agcpartners.co.uk', ' # ')
        ans = '<span class="active">HOME</span>'
        self.assertEqual(ans, generate_bc(*test))

    def test_home_page_index(self):
        test = ('https://www.agcpartners.co.uk/index.html', ' >>> ')
        ans = '<span class="active">HOME</span>'
        self.assertEqual(ans, generate_bc(*test))

    def test_long(self):
        # noinspection SpellCheckingInspection
        test = ('linkedin.it/'
                'kamehameha-from-bioengineering/'
                'or-paper-skin-of-biotechnology-a-with-at-the-the-to-a-surfer/'
                'cauterization-for-immunity-cauterization/'
                'pictures-you-wished-you-never-saw-but-you-cannot-unsee-now/'
                'funny.php',
                ' - ')

        a = '/kamehameha-from-bioengineering'
        b = '/or-paper-skin-of-biotechnology-a-with-at-the-the-to-a-surfer'
        c = '/cauterization-for-immunity-cauterization'
        # noinspection SpellCheckingInspection
        d = '/pictures-you-wished-you-never-saw-but-you-cannot-unsee-now'

        # noinspection SpellCheckingInspection
        ans = '<a href="/">HOME</a> - ' \
              f'<a href="{a}/">KAMEHAMEHA FROM BIOENGINEERING</a> - ' \
              f'<a href="{a}{b}/">PSBS</a> - ' \
              f'<a href="{a}{b}{c}/">CIC</a> - ' \
              f'<a href="{a}{b}{c}{d}/">PYWYNSBYCUN</a> - ' \
              '<span class="active">FUNNY</span>'
        self.assertEqual(ans, generate_bc(*test))
