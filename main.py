#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, Menu, colorchooser as cc, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd

import phonenumbers
from phonenumbers import geocoder, carrier

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""

    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.__init_config()
        self.__init_vars()
        self.__init_UI()
        self.__init_events()

    #------------------------------------------
    # Instance Variables
    #------------------------------------------
    def __init_vars(self):
        pass

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def __init_config(self):
        self.resizable(False, False)
        self.title('Phone Number Info Version 1.0')
        self.iconbitmap('python.ico')
        self.__STYLE = ttk.Style(self)
        self.__STYLE.theme_use('clam')

    #-------------------------------------------
    # Window Events / Keyboard Shorcuts
    #-------------------------------------------
    def __init_events(self):
        pass

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def __init_UI(self):
        self.__FRAME = ttk.Frame(self)
        self.__FRAME.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        __FIELDSET = ttk.LabelFrame(self.__FRAME, text='Get Phone Number Information')
        __FIELDSET.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        options = ['+63']
        self.country_code = tk.StringVar()
        self.country_code.set('+63')
        DROPDOWN = ttk.OptionMenu(__FIELDSET, self.country_code, *options)
        DROPDOWN.grid(row=0, column=0)

        self.number = tk.StringVar()
        ENTRY = ttk.Entry(__FIELDSET, width=50, textvariable=self.number)
        ENTRY.grid(row=0, column=1, ipady=5)
        ENTRY.focus()

        BUTTON = ttk.Button(self.__FRAME, text='Track', command=self.get_info)
        BUTTON.pack(side=tk.RIGHT, padx=(0, 10), pady=(0, 10))

    # ------------------------------------------
    def get_info(self):
        number = f'{self.country_code.get()}{self.number.get()}'

        ## country
        country_name = phonenumbers.parse(number, 'CH')
        get_country_name = geocoder.description_for_number(country_name, 'en')

        ## service provider
        service_number = phonenumbers.parse(number, 'RO')
        get_service_provider = carrier.name_for_number(service_number, 'en')

        prompt = f'''
            Country Name: {get_country_name}
            Servide Provider: {get_service_provider}
            '''

        mb.showinfo('Information', prompt)


#===========================
# Start GUI
#===========================

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()