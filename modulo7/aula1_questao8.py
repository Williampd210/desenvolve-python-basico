def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return "Número Inválido"
    cpf_base = cpf[:9]
    soma1 = sum(int(digito) * multiplicador for digito, multiplicador in zip(cpf_base, range(10, 1, -1)))
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1
    cpf_base += str(digito1)
    soma2 = sum(int(digito) * multiplicador for digito, multiplicador in zip(cpf_base, range(11, 1, -1)))
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2
    if cpf[-2:] == f"{digito1}{digito2}":
        return "Válido"
    else:
        return "Inválido"
cpf_usuario = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")
print(validar_cpf(cpf_usuario))
