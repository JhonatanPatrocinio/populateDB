import MySQLdb
from faker import Faker
import random
import datetime

faker = Faker('pt-BR')

def menu():
    print('1 - ADD COLLETION WITH MOVIE TABLE')
    print('2 - ADD CLIENT, PAYMENTS AND SIGNATURE LINKED')
    print('3 - ADD AVALIACOES')
    print('4 - ADD ACESSO')
    print('0 - SAIR')
    return int(input('Choose one option: '))

def subMenu():
    print('1 - ADD PAYMENT ON DAY')
    print('2 - ADD PAYMENT BEFORE PAY DAY')
    return int(input('Choose one option: '))


def addCollection(genre, type_collection, id_movie):
    COL_YEAR, COL_PRODUCER_YEAR = dateOfIncludeNerdFlixAndDateProducer()
    add_acervo = "INSERT INTO collections (COL_TITLE, COL_YEAR, COL_TYP_COL_ID, COL_GEN_ID, COL_PRODUCER_YEAR, COL_PRODUCER_NAME, COL_MOV_ID) \
    VALUES (\'%s \', %s , %s, %s, %s, \'%s\', %s)" % (
        faker.sentence(nb_words=3, variable_nb_words=True),
        faker.year(),
        type_collection,
        genre,
        faker.year(),
        faker.company(),
        id_movie
    )
    return add_acervo

def addClient():
    add_client = "INSERT INTO clients (CLI_NAME, CLI_RG, CLI_CPF, CLI_EMAIL, CLI_RG_UF, CLI_RG_ORG) \
    VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')" % (
        faker.name(),
        faker.rg(),
        faker.cpf(),
        faker.email(),
        faker.estado_sigla(),
        faker.cryptocurrency_code()
    )
    return add_client

def addMovie():
    add_movie = "INSERT INTO movies (MOV_MOVIE) VALUE (\'%s\')" % faker.file_path(extension='mkv')
    return add_movie

def addPayment(payDate, payDay, payPrice):
    add_payment = "INSERT INTO payments (PAY_DATE, PAY_DAY, PAY_PRICE) \
    VALUES (\'%s\', \'%s\', %s)" % (
        payDate,
        payDay,
        payPrice
    )
    return add_payment

def addContracts(paymentID, planID, cliID):
    dateInitial, dateFinal = dateContracts()
    add_contracts = "INSERT INTO contracts (CON_DATE_INITIAL, CON_DATE_FINAL, CON_PAY_ID, CON_PLA_ID, CON_CLI_ID ) \
    VALUES (\'%s\', \'%s\', %s, %s, %s)" % (
        dateInitial,
        dateFinal,
        paymentID,
        planID,
        cliID
    )
    return add_contracts

def addRating(colID, cliID):
    add_rating = "INSERT INTO ratings (RAT_COL_ID, RAT_CLI_ID, RAT_VALUE) \
    VALUES (%s, %s, %s)" % (
        colID,
        cliID,
        ratingValue()
    )
    return add_rating

def ratingValue():
    number = random.randrange(0, 6)
    return number

def dateContracts():
    dateInitial = faker.date_between(start_date="-30d", end_date='today')
    dateInitialconverted = '{}'.format(dateInitial)
    dateFinal = faker.date_between(start_date="+30d", end_date='+50d')
    dateFinalconverted = '{}'.format(dateFinal)
    return dateInitialconverted, dateFinalconverted

def paymentOnDay(payPrice):
    date = faker.date_between(start_date="-30d", end_date='today')
    dateconverted = '{}'.format(date)
    payment_sql_data = addPayment(dateconverted, dateconverted, payPrice)
    return payment_sql_data

def paymentBeforePayDay(payPrice):
    datePayDay = faker.date_between(start_date="-30d", end_date='+10d')
    datePayDayconverted = '{}'.format(datePayDay)
    while True:
        datePayDate = faker.date_between(start_date="-30d", end_date='+10d')
        if datePayDay < datePayDate:
            payPrice += payPrice * 0.05
            payment_sql_data = addPayment(datePayDate, datePayDay, payPrice)
            break
    return payment_sql_data

def returnPlaIDAndPlaPrice(allResults):
    idPlan = returnOneResult(allResults)
    for result in allResults:
        if result[0] == idPlan:
            plaPrice = result[1]
            break
    print(idPlan, plaPrice)
    return idPlan, plaPrice

def returnOneResult(allResults):
    number = random.choice(allResults)[0]
    if number:
        return number
    else:
        raise AssertionError()


def dateOfIncludeNerdFlixAndDateProducer():
    yearOfIncludeNerdFlix = faker.year()
    while True:
        dateProducer = faker.year()
        if dateProducer < yearOfIncludeNerdFlix:
            return yearOfIncludeNerdFlix, dateProducer


query_genre_cod = ("""SELECT GEN_ID FROM genre""")
query_type_colletion_cod = ("""SELECT TYP_COL_ID FROM type_collections""")
query_client_id = ("""SELECT CLI_ID FROM clients""")
query_collection_id = ("""SELECT COL_ID FROM collections""")
query_max_id_movies = ("""SELECT MAX(MOV_ID) FROM movies""")
query_max_id_clients = ("""SELECT MAX(CLI_ID) FROM clients""")
query_max_id_payments = ("""SELECT MAX(PAY_ID) FROM payments""")
query_plans = ("""SELECT PLA_ID, PLA_PRICE FROM plans""")

def main():
    try:
        cnx = MySQLdb.connect(host='localhost',
         user='root', passwd='1995', db='nerd_flix', port=3306)
        cursor = cnx.cursor()

    except MySQLdb.MySQLError as err:
        print(err)

    condition = -1
    while condition != 0:
        choice = menu()
        if choice == 1:
            try:
                cnx.query(query_genre_cod)
                resultsGenre = cnx.store_result()
                allResultsGenre = resultsGenre.fetch_row(maxrows=0)

                cnx.query(query_type_colletion_cod)
                resultsTypeColletion = cnx.store_result()
                allResultsTypeColletion = resultsTypeColletion.fetch_row(maxrows=0)

                movie_sql_data = addMovie()
                print(movie_sql_data)
                cursor.execute(movie_sql_data)
                cnx.commit()

                cnx.query(query_max_id_movies)
                resultsMoviesId = cnx.store_result()
                resultsNumberOfIdInMovies = resultsMoviesId.fetch_row(maxrows=0)
                idMovie = int(resultsNumberOfIdInMovies[0][0])
                cnx.commit()

                acervo_sql_data = addCollection(returnOneResult(allResultsGenre), returnOneResult(allResultsTypeColletion), idMovie)
                print(acervo_sql_data)
                cursor.execute(acervo_sql_data)

                f = open('inserts.txt', 'r')
                dados = f.readlines()
                dados.append('{};\n'.format(movie_sql_data))
                dados.append('{};\n'.format(acervo_sql_data))
                f = open('inserts.txt', 'w')
                f.writelines(dados)
                f.close()
                cnx.commit()
            
            except MySQLdb.MySQLError as err:
                print(err) 

        elif choice == 2:
            try:
                client_sql_data = addClient()
                print(client_sql_data)
                cursor.execute(client_sql_data)
                cnx.commit()

                cnx.query(query_max_id_clients)
                resultsClientsID = cnx.store_result()
                resultsNumberOfIDMovies = resultsClientsID.fetch_row(maxrows=0)
                idClient = int(resultsNumberOfIDMovies[0][0])
                cnx.commit()

                cnx.query(query_plans)
                resultsPlans = cnx.store_result()
                allResultsPlans = resultsPlans.fetch_row(maxrows=0)
                print(allResultsPlans)
                idPlan, payPrice = returnPlaIDAndPlaPrice(allResultsPlans)

                choicesubMenu = subMenu()
                if choicesubMenu == 1:
                    payment_sql_data = paymentOnDay(payPrice)
                elif choicesubMenu == 2:
                    payment_sql_data = paymentBeforePayDay(payPrice)
                print(payment_sql_data)
                cursor.execute(payment_sql_data)
                cnx.commit()

                cnx.query(query_max_id_payments)
                resultsPaymentsID = cnx.store_result()
                resultsNumberOfIDPayments = resultsPaymentsID.fetch_row(maxrows=0)
                idPayment = int(resultsNumberOfIDPayments[0][0])
                cnx.commit()

                contract_sql_data = addContracts(idPayment, idPlan, idClient)
                print(contract_sql_data)
                cursor.execute(contract_sql_data)
                cnx.commit()


                f = open('inserts.txt', 'r')
                dados = f.readlines()
                dados.append('{};\n'.format(client_sql_data))
                dados.append('{};\n'.format(payment_sql_data))
                dados.append('{};\n'.format(contract_sql_data))
                f = open('inserts.txt', 'w')
                f.writelines(dados)
                f.close()
                cnx.commit()
            except MySQLdb.MySQLError as err:
               print(err)
        elif choice == 3:
            cnx.query(query_client_id)
            resultsClientsID = cnx.store_result()
            allResultsClientsID = resultsClientsID.fetch_row(maxrows=0)

            cnx.query(query_collection_id)
            resultsColletionsID = cnx.store_result()
            allResultsCollectionsID = resultsColletionsID.fetch_row(maxrows=0)

            rating_sql_data = addRating(returnOneResult(allResultsCollectionsID), returnOneResult(allResultsClientsID))
            cursor.execute(rating_sql_data)
            print(rating_sql_data)
            cnx.commit()
            
            f = open('inserts.txt', 'r')
            dados = f.readlines()
            dados.append('{};\n'.format(rating_sql_data))
            f = open('inserts.txt', 'w')
            f.writelines(dados)
            f.close()
            cnx.commit()
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 0:
            exit()

if __name__ == '__main__':
    main()
