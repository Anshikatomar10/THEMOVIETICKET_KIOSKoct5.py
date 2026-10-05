# THE MOVIE TICKET KIOSK .
#You are writing a automated ticketing system for available movies, handle quantities , prevent numbers , and 
#keep track of sales.
#THE MOVIE DICTIONARY AND ACCUMULATORS:Create a single dictionary called movies with these titles and ticket
# prices .        ."matrix":12.00, "avatar":15.00 , "shrek":8.00
#create 2 accumulator variables set to 0 :total_tickets_sold and total_revenue .
#THE MAIN LOOP & EXIT :Create continious while true:loop .
#promt the user "enter the movie you want to see (or 'exit' to close ):"
# if they type 'exit' , break the loop.
#promt the user for the number of tickets .
 
shows ={"matrix":12.00,
         "avatar":15.00,
         "shrek":8.00,
         }

total_tickets_sold = 0
total_revenue = 0

while True:
    price = 0
    movie= str(input("enter the movie you want to see (or enter 'exit' to close): ")).lower().strip()
    if movie == "exit":
        break
    if movie in shows:
        price = shows[movie]
        while True:
            try:
                 quantity = int(input("enter the number of tickets you want in whole numbers :"))
                 break
            except ValueError:
                print("invalid response ,please enter a whole number (like1,2,3) :")
    else:
        print("sorry for inconvinience , this movie is not available.")
    total_price = price*quantity
    print("your total is :$", total_price)
    total_tickets_sold += quantity
    total_revenue += total_price 

print("your total number of tickets sold today are :", total_tickets_sold) 
print("your today's revenue is :$", total_revenue)                 
