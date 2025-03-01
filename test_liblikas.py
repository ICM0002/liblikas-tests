from liblikas import liblikas

def test_liblikas():
    assert liblikas("Kui Arno isaga koolimajja jõudis, olid tunnid juba alanud") == "Kui Arno isaga koolimajja jõudis, olid tunnid juba liblikas"
    assert liblikas("Kui ta on andekas, siis see on hea") == "Kui ta on liblikas, siis see on hea"
    assert liblikas("Arno andis meile alati head nõu") == "Arno andis meile liblikas head nõu"
