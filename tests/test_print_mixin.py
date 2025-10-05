from src.products import Product, Smartphone, LawnGrass

def test_print_mixin_product(capsys):
    Product('Bread', 'local', 5.8, 2)     # печать происходит сейчас
    out = capsys.readouterr().out         # читаем сразу после создания
    assert "Product('Bread', 'local', 5.8, 2)" in out

def test_print_mixin_smart(capsys):
    Smartphone('Samsung', 'local', 5.8, 2, "AAA", "S20FE", 64, "white")     # печать происходит сейчас
    out = capsys.readouterr().out         # читаем сразу после создания
    assert "Smartphone('Samsung', 'local', 5.8, 2, 'AAA', 'S20FE', 64, 'white')" in out

def test_print_mixin_lawn(capsys):
    LawnGrass('Grass', 'local', 5.8, 2, 'China', 2, 'green')     # печать происходит сейчас
    out = capsys.readouterr().out         # читаем сразу после создания
    assert "LawnGrass('Grass', 'local', 5.8, 2, 'China', 2, 'green')" in out