import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(10, alku_saldo = -10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_nolla_kun_arvo_virheellinen(self):
        self.varasto = Varasto(-2)

        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)

    def test_alku_saldo_nolla_kun_arvo_virheellinen(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0.0)

    def test_lisays_ei_lisaa_saldoa_kun_negatiivinen(self):
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_saldo_tilavuus_kun_suurempaa_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_ottaa_varastosta_vahemman_kuin_nolla_nollaantuu(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_kun_maara_pienempi_kuin_nolla_niin_nolla(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_kun_maara_suurempi_kuin_saldo_otetaan_kaikki_mita_voidaan(self):
        alkutalletus = 8
        self.varasto.lisaa_varastoon(alkutalletus)

        saatu_maara = self.varasto.ota_varastosta(9)
        self.assertAlmostEqual(saatu_maara, alkutalletus)  

    def test_palauttaa_oikein(self):
        self.varasto.lisaa_varastoon(8)

        self.assertEqual(str(self.varasto), "saldo = 8, vielä tilaa 2")



