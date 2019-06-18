import MySQLdb
from faker import Faker
import random
import datetime

faker = Faker('pt-BR')

def addClienteData(munCodigo):
    add_clientes = ("INSERT INTO clientes "
                    "(CLI_MUN_CODIGO, CLI_NOME, CLI_DATA_NASCIMENTO,"
					 "CLI_SEXO, CLI_CPF, CLI_RG, CLI_CNPJ, CLI_ENDERECO, CLI_EMAIL,"
					 "CLI_DATA_CADASTRO, CLI_TIPO, CLI_STATUS, CLI_FONE, CLI_NOME_CONTATO) "
                    "VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')" % (munCodigo,
                                                                                    faker.name_male(),
                                                                                    fakerDateBirth(),
                                                                                    'M',
                                                                                    faker.cpf(),
                                                                                    faker.rg(),
                                                                                    faker.cnpj(),
                                                                                    fakerEndereco(),
                                                                                    faker.email(),
                                                                                    fakerDateJoined(),
                                                                                    "F",
                                                                                    "A",
                                                                                    faker.cellphone_number(),
                                                                                    faker.name_male()
                                                                                    )
                    )
    return add_clientes

def addFornecedorData(munCodigo):
    add_fornecedor = ("INSERT INTO fornecedores "
     "(FOR_MUN_CODIGO, FOR_RAZAO_SOCIAL, FOR_NOME_FANTASIA,"
     "FOR_NOME_CONTATO, FOR_CNPJ, FOR_ENDERECO,"
     "FOR_DATA_CADASTRO, FOR_FONE, FOR_EMAIL, FOR_WEBSITE) "
     "VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')" % (
     munCodigo,
     faker.company(),
     faker.bs(),
     faker.name(),
     faker.cnpj(),
     fakerEndereco(),
     fakerDateJoined(),
     faker.cellphone_number(),
     faker.company_email(),
     faker.url()
     )
     )
    return add_fornecedor

def addMunicipios():
    add_municipio = (
        "INSERT INTO municipios"
        "(MUN_NOME, MUN_UF_ESTADO, MUN_CEP)"
        "VALUES (\'%s\', \'%s\', \'%s\')" % (
        faker.city(),
        faker.estado_sigla(),
        faker.postcode()
    )
    )
    return add_municipio

def addAtendentes():
    add_atendentes = (
        "INSERT INTO atendentes"
        "(ATE_NOME, ATE_ULTIMO_ACESSO, ATE_RAMAL, ATE_EMAIL, ATE_PERFIL, ATE_STATUS)"
        "VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')" % (
        faker.name(),
        fakerDateJoined(),
        faker.year(),
        faker.email(),
        'V',
        'A'
    )
    )
    return add_atendentes

def returnOneMunCodigo(allResults):
    number = random.choice(allResults)[0]
    if number:
        return number
    else:
        raise AssertionError()

def fakerEndereco():
    s = '%s - %s' % (faker.street_address(), faker.bairro())
    return s

def fakerDateBirth():
    date = faker.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=115)
    dateconverted = '{}'.format(date)
    return dateconverted

def fakerDateJoined():
    date = faker.date_time_between(start_date="-30d", end_date='now')
    dateconverted = '{}'.format(date)
    return dateconverted





query_mun_codigo = ("""SELECT MUN_CODIGO FROM municipios""")

def main():
    try:
        cnx = MySQLdb.connect(host='localhost',
         user='root', passwd='1995', db='db_vendas', port=3306)

        cursor = cnx.cursor()
        cnx.query(query_mun_codigo)
        resultsMunicipios = cnx.store_result()
        allResultsMunicipios = resultsMunicipios.fetch_row(maxrows=0)
        # ADD CLIENTE
        # cliente_data = addClienteData(returnOneMunCodigo(allResultsMunicipios))
        # print(cliente_data)
        # cursor.execute(cliente_data)

        # ADD FORNECEDOR
        # fornecedor_data = addFornecedorData(returnOneMunCodigo(allResultsMunicipios))
        # print(fornecedor_data)
        # cursor.execute(fornecedor_data)

        #ADD MUNICIPIOS
        # municipio_data = addMunicipios()
        # print(municipio_data)
        # cursor.execute(municipio_data)

        #ADD ATENDENTES
        atendente_data = addAtendentes()
        print(atendente_data)
        cursor.execute(atendente_data)
        cnx.commit()

    except MySQLdb.MySQLError as err:
        print(err)


if __name__ == '__main__':
    main()
