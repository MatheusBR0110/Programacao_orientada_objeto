from conta import Conta

conta1 = Conta(535, "Ricardo", 55.0, 5000.0)
conta2 = Conta(555, "Luana", 100.0, 1000.0)

conta1.transferir(20, conta2)
conta1.extrato()