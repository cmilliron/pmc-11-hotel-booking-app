import pandas as pd
from pprint import pprint


class Hotel:
    def __init__(self, id, df):
        self.id = id
        self.name = df[df['id'] == id].iloc[0]['name']
        self.city = df[df['id'] == id].iloc[0]['city']
        self.capacity = int(df[df['id'] == id].iloc[0]['capacity'])
        self.available = df[df['id'] == id].iloc[0]['available']
        self.df = df

    def book(self):
        try:
            print(f'Your trip is booked in {self.name}')
            self.available = False
            index = df.loc[self.df['id'] == self.id].index[0]
            self.df.at[index, "available"] = 'no'
            # print(df.loc[self.df['id'] == self.id].index)
            print(self.df)
            self.df.to_csv('hotels_test.csv', index=False)
            return True
        except Exception as e:
            print(f"There was an error: {e}")
            return False


    def is_available(self):
        if self.available == 'yes':
            return True
        else:
            return False

    @staticmethod
    def list_hotels(df):
        print('{0: <6}'.format("ID")
              + '{0: <30}'.format("Name")
              + '{0: <15}'.format("City")
              + '{0: <12}'.format("Capacity")
              + '{0: <12}'.format("Available"))
        for row in df.iterrows():
            # pprint(row[1]['id'])
            print('{0: <6}'.format(str(row[1]['id']))
                  + '{0: <30}'.format(row[1]['name'])
                  + '{0: <15}'.format(row[1]['city'])
                  + '{0: <12}'.format(str(row[1]["capacity"]))
                  + '{0: <12}'.format(row[1]['available']))


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer = customer_name
        self.hotel = hotel_object

    def generate(self):
        is_booked = self.hotel.book()
        if is_booked:
            print(f"Thank you {self.customer}.\nYour reservation at {self.hotel.name} is confirmed.")
        else:
            print("There was a problem.")


if __name__ == "__main__":
    df = pd.read_csv('hotels.csv')

    Hotel.list_hotels(df)
    id = int(input('Enter the id of the hotel: '))
    hotel = Hotel(id, df)
    print(hotel.name, hotel.city)
    if hotel.is_available():
        name = input('\nEnter your name: ')
        reservation_ticket = ReservationTicket(name, hotel)
        reservation_ticket.generate()
    else:
        print("\nHotel is not free.")