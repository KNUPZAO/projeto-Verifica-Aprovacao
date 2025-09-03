def verificar_aprovacao(lista_de_notas,media_corte):
    print('---Verificar situação dos alunos---')
    for nota in lista_de_notas:
        if nota >= media_corte:
            print(f'nota {nota}: aprovado')
        else:
            print(f'nota {nota}: reprovado')

#usando a função:
notas_semestre = [4.5, 7.0, 9.5, 6.0]
verificar_aprovacao(notas_semestre, 7.0)           