import unittest
from social import BskyPostJoiner, BskyPostData, get_sld_tld


class TestBskyPostJoiner(unittest.TestCase):
    def test_post_joiner(self):
        post_joiner = BskyPostJoiner()
        post_data = BskyPostData(
            "Kde odpočívá včelí královna? I to odhalili autonomní mikroroboti z pražského ČVUT",
            "https://www.ceskatelevize.cz/clanky/kde-odpociva-vceli-kralovna-i-to-odhalili-autonomni-mikroroboti-z-prazskeho-cvut")
        post_data2 = BskyPostData(
            "Dvě třetiny českých nemocnic už používají umělou inteligenci",
            "https://www.wired.cz/clanky/dve-tretiny-ceskych-nemocnic-uz-pouzivaji-umelou-inteligenci")
        post_data3 = BskyPostData(
            "Český vědec zjistil, že většina lidí je schopna zvládnout jen 4 úkoly najednou",
            "https://www.wired.cz/clanky/cesky-vedec-zjistil-ze-vetsina-lidi-je-schopna-zvladnout-jen-4-ukoly-najednou")
        post_data4 = BskyPostData(
            "Britská policie vyšetřuje požár u DHL. Podezřívá ruské agenty z umístění zápalného zařízení do balíku",
            "https://www.irozhlas.cz/clanky/britska-policie-vysetruje-pozar-u-dhl-podezriva-ruske-agenty-z-umisteni-zapalneho-zarizeni-do-baliku")
        post_publisher = None
        post_joiner.add_post(post_data, publisher=post_publisher)
        self.assertEqual(1, len(post_joiner.posts))
        self.assertEqual(post_data.get_length(), post_joiner.total_length)
        post_joiner.add_post(post_data2, publisher=post_publisher)
        self.assertEqual(2, len(post_joiner.posts))
        post_joiner.add_post(post_data3, publisher=post_publisher)
        self.assertEqual(3, len(post_joiner.posts))
        post_joiner.add_post(post_data4, publisher=post_publisher)
        self.assertEqual(1, len(post_joiner.posts))
        print('\n\n\n')
        post_joiner.create_joined_posts_and_publish(publisher=post_publisher)


class TestDomainParser(unittest.TestCase):
    def test_domain_parser(self):
        self.assertEqual("wired.cz", get_sld_tld("www.wired.cz"))
        self.assertEqual("wired.cz", get_sld_tld("wired.cz"))
        self.assertEqual("wired.cz", get_sld_tld("https://wired.cz"))
        self.assertEqual("wired.cz", get_sld_tld("https://www.wired.cz"))
        self.assertEqual("wired.cz", get_sld_tld("https://www.wired.cz/"))
        self.assertEqual("wired.cz", get_sld_tld("https://www.wired.cz/clanky"))
        self.assertEqual("wired.cz", get_sld_tld("https://www.wired.cz/clanky/"))
        self.assertEqual("wired.cz", get_sld_tld("https://www.wired.cz/clanky/nejlepsi-clanky"))
        self.assertEqual("ceskatelevize.cz", get_sld_tld("https://www.ceskatelevize.cz/"))
        self.assertEqual("irozhlas.cz", get_sld_tld("https://www.irozhlas.cz/OVEROVNA/"))
