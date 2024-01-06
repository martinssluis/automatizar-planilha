import openpyxl

#carregar arquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')
#selecionar uma página
frutas_page = book['Frutas']
#imprimindo os dados de cada linha
for rows in frutas_page.iter_rows(min_row=2,max_row=5):
     print(f'{rows[0].value}, {rows[1].value}, {rows[2].value}') #para exibir tudo na mesma linha

    #para alterar algum valor da planilha
    # for cell in rows:
    #     if cell.value == 'Banana':
    #         cell.value = 'Fruta 1'


#salvar as alterações como outra planilha
    #book.save('Planilha de Compras v2.xlsx')

