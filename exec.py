from conta import Conta

conta1 = Conta(535, "Ricardo", 55.0, 5000.0)
conta2 = Conta(555, "Luana", 100.0, 1000.0)

conta1.set_limite(2000)
print(conta1.get_limite())