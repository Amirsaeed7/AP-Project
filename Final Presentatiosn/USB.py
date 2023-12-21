import sqlite3
#this is gonna be a module that we can use it's functions
#connect the database
conn = sqlite3.connect('USB.db')
#Create a cursor
cursor = conn.cursor()

def Check_For_Product(Product_Name , search_bool):
    Products_Name = []
    if search_bool == False:    
        cursor.execute("SELECT * FROM Details")
        for m in cursor.fetchall():
            Products_Name.append(m[0])
        if Product_Name in Products_Name:
            return True
        else:
            return False
    else:
        cursor.execute('SELECT Name FROM Details')
        Products_Name = cursor.fetchall()
        List_Of_Products = [i[0] for i in Products_Name]
        Match = [name for name in List_Of_Products if Product_Name.lower() in name.lower()]
        return Match
def Show_Details(Product_Name):
    cursor.execute("SELECT * FROM Details WHERE Name = '{}'".format(Product_Name))
    Details = cursor.fetchall()[0]
    return Details[0], Details[1], Details[2], Details[3], Details[4], Details[5], Details[6]

def Get_Product(Product_Name, Product_Storage, Product_Speed, Product_Version, Product_Digikala,Product_MeghdadIt,Product_TechnoSun, Product_Page):
    Details = []
    Details.append(Product_Name)
    Details.append(Product_Storage)
    Details.append(Product_Speed)
    Details.append(Product_Version)
    Details.append(Product_Digikala)
    Details.append(Product_MeghdadIt)
    Details.append(Product_TechnoSun)
    Details.append(Product_Page)
    Details.append(1)
    cursor.execute("INSERT INTO Details VALUES (?,?,?,?,?,?,?,?,?)" , Details)
    conn.commit()
def Update_Price(Product_Name,Product_Digikala, Product_MeghdadIt, Product_TechnoSun):
    cursor.execute("UPDATE Details SET Digikala ='{}' WHERE Name = '{}'".format(Product_Digikala, Product_Name))
    cursor.execute("UPDATE Details SET MeghdadIt ='{}' WHERE Name = '{}'".format(Product_MeghdadIt, Product_Name))
    cursor.execute("UPDATE Details SET TechnoSun ='{}' WHERE Name = '{}'".format(Product_TechnoSun, Product_Name))
    conn.commit()