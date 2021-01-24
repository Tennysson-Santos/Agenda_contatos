AGENDA = {}

AGENDA['Tennysson Santos'] = {
'telefone': '99178-4135',
'email': 'tennyssonsantos@gmail.com',
'cidade': 'Atibaia-SP'

}


AGENDA['Soraia Santos'] = {
'telefone': '99123-2333',
'email': 'sory_santana@gmail.com',
'cidade': 'Atibaia-SP'

}


def mostrar_agenda():
	for contato in AGENDA:
		print('---'*12)
		buscar_contato(contato)


def buscar_contato(contato):
	print('Nome:', contato)
	print('Telefone:', AGENDA[contato]['telefone'])
	print('Email:', AGENDA[contato]['email'])
	print('Cidade:', AGENDA[contato]['cidade'])

def ler_detalhes_contato():
	telefone = (input('Digite seu Telefone: '))
	email = input('Digite seu Email:')
	cidade = (input('Digite sua Cidade: '))
	return telefone, email, cidade
	
def incluir_editar_contato(contato, telefone, email, cidade):
	AGENDA[contato]= {
	'telefone': telefone,
	'email': email,
	'cidade': cidade,
	
    }
	salvar()
	print(f'\n>>> Contato {contato} incluido\editado com sucesso! <<<')
	
	
def excluir_contato(contato):
	AGENDA.pop(contato)
	salvar()
	print(f'>>> Contato {contato} excluido com sucesso! <<<')
	
	
	
def exportar_contatos(nome_do_arquivo):
	try:
		with open(nome_do_arquivo, 'w') as arquivo:
			for contato in AGENDA:
				telefone = AGENDA[contato]['telefone']
				email = AGENDA[contato]['email']
				cidade = AGENDA[contato]['cidade']
				arquivo.write(f'{contato},{telefone},{email},{cidade}\n')
		print('>>> Contatos exportados com sucesso!')
	except:
		print('>>> Ocorreu algum problema com a exportação...')


def importar_arquivo(nome_do_arquivo):
	try:
		with open(nome_do_arquivo, 'r') as arquivo:
			linhas = arquivo.readlines()
			for linha in linhas:
				detalhes = linha.strip()(',')
				contato = detalhes[0]
				telefone = detalhes[1]
				email = detalhes[2]
				cidade = detalhes[3]
				incluir_editar_contato(contato,telefone,email,cidade)
	except:
		print('>>> Arquivo não encontrato')
		
def salvar():
	exportar_contatos('database.csv')
	
def carregar():
	try:
		with open('database.csv','r') as arquivo:
			linhas = arquivo.readlines()
			for linha in linhas:
				detalhes = linha.strip().split(',')

				contato = detalhes[0]
				telefone = detalhes[1]
				email = detalhes[2]
				cidade = detalhes[3]

				AGENDA[contato] = {
					'telefone': telefone,
					'email': email,
					'cidade': cidade,
				}
		print('>>>> Database carregado com sucesso')
		print('>>>> {} contatos carregados'.format(len(AGENDA)))
	except FileNotFoundError:
		print('>>>> Arquivo não encontrado')
	except Exception as error:
		print('>>>> Algum erro inesperado ocorreu')	
		print(error)
	

def imprimir_menu():
	print('\n<#> MENU AGENDA 2021 <#>\n')
	print('[1] Mostrar Agenda')
	print('[2] Buscar Contato')
	print('[3] Incluir\Editar Contato')
	print('[4] Excluir Contato')
	print('[5] Exportar contatos em CSV')
	print('[6] Importar arquivo .CSV')
	print('[0] Sair')


#inicio do Programa				
carregar()
while True:
	imprimir_menu()
	menu = input('\nEscolha uma opção: ')
	print()
	if menu == '1':
		mostrar_agenda()
		print()
	elif menu == '2':
		try:
			contato = str(input('\nDigite nome do contato: '))
			buscar_contato(contato)
		except KeyError:
			print('>>> Esse contato não existe! <<<')
		

	elif menu == '3':
		try:
			contato = (input('Digite seu Nome: '))
			AGENDA[contato]
			print('Editando contato...', contato)
		except KeyError:
			print('Incluindo contato...', contato)
			telefone, email, cidade = ler_detalhes_contato()
			incluir_editar_contato(contato, telefone, email, cidade)
		
		
	elif menu == '4':
		try:
			contato = (input('Digite o contato para Excluir: '))
			excluir_contato(contato)
		except KeyError:
			print('>>> Esse contato não existe! <<<')
			
	elif menu == '5':
		nome_do_arquivo = input('Digite o arquivo a ser exportado: ')
		exportar_contatos(nome_do_arquivo)
		
	elif menu == '6':
		nome_do_arquivo = input('Digite o arquivo a ser importado: ')
		importar_arquivo(nome_do_arquivo)
		

	elif menu == '0':
		print('\nVocê saiu do programa...')
		break
	
	else:
		print('Opção invalida!')
		

