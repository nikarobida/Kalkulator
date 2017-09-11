import tkinter as tk

class Kalkulator:

    def __init__(self, okno):
        self.pripravi_graficni_vmesnik(okno)
        
    def zamenjaj_besedilo(self, besedilo):
        self.prikaz.delete(0, tk.END)
        self.prikaz.insert(0, besedilo)

    def zapisi_na_prikaz(self, besedilo):
        self.besedilo_v_prikazu = self.prikaz.get()
        self.dolzina_besedila_v_prikazu = len(self.besedilo_v_prikazu)

        if self.besedilo_v_prikazu == '0':
            self.zamenjaj_besedilo(besedilo)
        else:
            self.prikaz.insert(self.dolzina_besedila_v_prikazu, besedilo)

    def izracunaj_izraz(self):
        self.besedilo_v_prikazu = self.prikaz.get()
        for znak in self.besedilo_v_prikazu:
            if znak == '+':
                k = self.besedilo_v_prikazu.find('+')
                stevilo1 = float(self.besedilo_v_prikazu[:k])
                stevilo2 = float(self.besedilo_v_prikazu[k + 1:])
                rezultat = stevilo1 + stevilo2
                self.osvezi_prikaz()
                self.zapisi_na_prikaz(rezultat)
            elif znak == '-':
                k = self.besedilo_v_prikazu.find('-')
                stevilo1 = float(self.besedilo_v_prikazu[:k])
                stevilo2 = float(self.besedilo_v_prikazu[k + 1:])
                rezultat = stevilo1 - stevilo2
                self.osvezi_prikaz()
                self.zapisi_na_prikaz(rezultat)
            elif znak == '*':
                k = self.besedilo_v_prikazu.find('*')
                stevilo1 = float(self.besedilo_v_prikazu[:k])
                stevilo2 = float(self.besedilo_v_prikazu[k + 1:])
                rezultat = stevilo1 * stevilo2
                self.osvezi_prikaz()
                self.zapisi_na_prikaz(rezultat)
            elif znak == '/':
                k = self.besedilo_v_prikazu.find('/')
                stevilo1 = float(self.besedilo_v_prikazu[:k])
                stevilo2 = float(self.besedilo_v_prikazu[k + 1:])
                rezultat = stevilo1 / stevilo2
                self.osvezi_prikaz()
                self.zapisi_na_prikaz(rezultat)
            elif znak == '%':
                k = self.besedilo_v_prikazu.find('%')
                stevilo1 = float(self.besedilo_v_prikazu[:k])
                rezultat = stevilo1 / 100
                self.osvezi_prikaz()
                self.zapisi_na_prikaz(rezultat)
            elif znak == '^':
                k = self.besedilo_v_prikazu.find('^')
                stevilo1 = float(self.besedilo_v_prikazu[:k])
                stevilo2 = float(self.besedilo_v_prikazu[k + 1:])
                rezultat = stevilo1 ** stevilo2
                self.osvezi_prikaz()
                self.zapisi_na_prikaz(rezultat)

    def zbrisi_zadnjo_stevko(self):
        l = len(self.besedilo_v_prikazu)
        self.zamenjaj_besedilo(self.besedilo_v_prikazu[: l])
    
    def osvezi_prikaz(self):
        self.zamenjaj_besedilo('0')

    def pripravi_graficni_vmesnik(self, okno):
        okvir = tk.Frame(okno)
        okvir.grid(row = 0, column = 0)
        self.prikaz = tk.Entry(okvir)
        self.prikaz.insert(0, '0')
        self.prikaz.grid(row = 0, column = 0, columnspan = 5)

        gumbi = tk.Frame(okno)
        gumbi.grid(row = 1, column = 0)
        b0 = tk.Button(gumbi, font = 11, text = '0', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('0'))
        b0.grid(row = 5, column = 0, columnspan = 2)
        b1 = tk.Button(gumbi, font = 11, text = '1', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('1'))
        b1.grid(row = 4, column = 0)
        b2 = tk.Button(gumbi, font = 11, text = '2', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('2'))
        b2.grid(row = 4, column = 1)
        b3 = tk.Button(gumbi, font = 11, text = '3', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('3'))
        b3.grid(row = 4, column = 2)
        b4 = tk.Button(gumbi, font = 11,text = '4', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('4'))
        b4.grid(row = 3, column = 0)
        b5 = tk.Button(gumbi, font = 11, text = '5', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('5'))
        b5.grid(row = 3, column = 1)
        b6 = tk.Button(gumbi, font = 11, text = '6', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('6'))
        b6.grid(row = 3, column=2)
        b7 = tk.Button(gumbi, font = 11, text = '7', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('7'))
        b7.grid(row = 2, column = 0)
        b8 = tk.Button(gumbi, font = 11, text = '8', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('8'))
        b8.grid(row = 2, column = 1)
        b9 = tk.Button(gumbi, font = 11, text = '9', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('9'))
        b9.grid(row = 2, column = 2)
                
        b_pika = tk.Button(gumbi, font = 11, text = '.', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('.'))
        b_pika.grid(row = 5, column = 2)
        b_plus = tk.Button(gumbi, font = 11, text = '+', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('+'))
        b_plus.grid(row = 5, column = 3)
        b_minus = tk.Button(gumbi, font = 11, text = '-', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('-'))
        b_minus.grid(row = 4, column = 3)
        b_krat = tk.Button(gumbi, font = 11, text = '*', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('*'))
        b_krat.grid(row = 2, column = 3)
        b_deljeno = tk.Button(gumbi, font = 11, text = '/', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('/'))
        b_deljeno.grid(row = 3, column = 3)
        b_odstotek = tk.Button(gumbi, font = 11, text = '%', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('%'))
        b_odstotek.grid(row = 3, column = 4)

        
        b_potenca = tk.Button(gumbi, font = 11, text = '^', borderwidth = 0, command = lambda: self.zapisi_na_prikaz('^'))
        b_potenca.grid(row = 1, column = 0)
        b_del = tk.Button(gumbi, text = 'DEL', borderwidth = 0, command = lambda: self.zbrisi_zadnjo_stevko())
        b_del.grid(row = 1, column = 1)
        b_enako = tk.Button(gumbi, font = 11, text = '=', borderwidth = 0, command = lambda: self.izracunaj_izraz())
        b_enako.grid(row = 4, column = 4, rowspan = 2)
        b_pocisti = tk.Button(gumbi, font = 11, text = 'C', borderwidth = 0, command = lambda: self.osvezi_prikaz())
        b_pocisti.grid(row = 2, column = 4)



okno = tk.Tk()
okno.title('Kalkulator')
kalkulator = Kalkulator(okno)
okno.mainloop()    

            

