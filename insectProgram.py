import insectClass as i

def main():
    housefly = i.insect()
    mosquito = i.insect()
    # determine distance of flight for each
    housefly.flight()
    mosquito.flight()
    # display results
    print(f'Housefly: {housefly.get_flight()}\nMosquito: {mosquito.get_flight()}')

main()