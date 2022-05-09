from handler import Handler
class App:
    def __init__(self):
        self.stocks = ['FB', 'GOOG', 'AMZN']
        self.api_key = 'x_XKl4T9U4DglUOnFeO_m9iU9gJiSQTP'
        
    def run(self):
        new_handler = Handler(self.api_key)
        print("\nWelcome!")
        new_handler.update_date()
        new_handler.create_stock_profile()
        while True:
            choice = input("\nEnter Command [ADD, REMOVE, STOCKS, CLEAR, END, UPDATE]\n:")
            
            if choice == 'ADD' or choice == 'add':
                print("ONLY ENTER UP TO 5 STOCKS")
                add_stock = input('\nEnter stock ticker to add:')
                add_target = input('\nEnter target price to add:')
                new_handler.add_stock(add_stock, add_target)
                print(f"\nAdded {add_stock.upper()} at price {add_target} to stock profile.")
                
            elif choice == 'REMOVE' or choice =='remove':
                remove_stock = input('\nEnter stock ticker to remove:')
                new_handler.remove_stock(remove_stock)
                print(f"\n Removed {remove_stock.upper()} from stock profile")
            
            elif choice == 'UPDATE' or choice == 'update':
                new_handler.update()
                
            elif choice == 'STOCKS' or choice == 'stocks':
                print("\nStock Profile:")
                stock_profile = new_handler.get_stock_profile()
                print()
                print('''YESTERDAY'S PRICES [TARGET, LOW, HIGH, OPEN, CLOSE]:\n''')
                print('------------------------------------------------')
                for stock in stock_profile:
                    print(f"{stock}: {stock_profile[stock]}")
                print('------------------------------------------------')
                
                print('\nAnalysis?')
                analysis = input('\Enter Command [ANALYSIS, BACK]\n:')
                if analysis == 'ANALYSIS' or analysis == 'analysis':
                    pass
                elif analysis == 'BACK' or analysis == 'back':
                    pass
                
            elif choice == 'CLEAR' or choice == 'clear':
                print("\nClearing stocks:")
                new_handler.db.clear_database()
                print("\nStocks clear!")
                
            elif choice == 'END' or choice == 'end':
                print('\nGoodbye!')
                break
            
            else:
                break
        
a = App()
a.run()
            
            