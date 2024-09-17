import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """Book a hotel by changing availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"]
                              == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        content = ""
        return content



print(df)
hotel_ID = input("Hotel ID: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free")