from liblikas import liblikas

def test_liblikas():
    assert liblikas("Kui Arno isaga koolimajja jõudis, olid tunnid juba alanud") == "Kui Arno isaga koolimajja jõudis, olid tunnid juba liblikas"
    assert liblikas("Kui ta on andekas, siis see on hea") == "Kui ta on andekas, siis see on liblikas"
    assert liblikas("Arno andis meile alati head nõu") == "Arno andis meile liblikas liblikas nõu"
    assert liblikas("Armas koht, aga kõik on alguses") == "Armas koht, aga kõik on liblikas"
