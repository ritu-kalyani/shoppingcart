from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter.ttk import Scrollbar
import tkinter.messagebox as MessageBox
from mysql.connector import Error
from PIL import ImageTk, Image
from operator import itemgetter
import smtplib
from random import randint


def backgroundImage(window, height, width):
    window.resizable(width=False, height=False)
    image = Image.open("C:/Users/ADMIN/Documents/python prg/mycart.png")

    image = image.resize((height, width), Image.ANTIALIAS)
    backgroundImg1 = ImageTk.PhotoImage(image)

    return backgroundImg1


def registerUser():
    # Submit for user
    def submit():
        u_name = user_name.get()
        passw = password.get()
        c_passw = confirm_password.get()
        f_name = first_name.get()
        l_name = last_name.get()

        gen = var.get()
        zipc = zipcode.get()
        que = queNumber.get()
        p_no = phone_no.get()
        em = email.get()
        answer = ans.get()

        if u_name == '' or passw == '' or c_passw == '' or f_name == '' or gen == '' or zipc == '' or p_no == '' or answer == '' or em == '':
            MessageBox.showinfo("Warning",
                                "All the fields marked with (*) are compulsory")
        if passw != c_passw:
            MessageBox.showinfo(
                'Warning', 'Password and confirm password does not match')

        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"
            )
            c = conn.cursor()
            defaultIsLoggedInValue = 'F'

            # Insert the record into the table
            user_data = "insert into user_info(user_name, password, first_name, last_name, gender, zipcode, email, que, ans, phone_no, isLoggedIn) values('" + u_name + "','" + passw + "','" + \
                        f_name + "','" + l_name + "','" + gen + "','" + zipc + "','" + \
                        em + "','" + que + "','" + answer + "','" + p_no + "','" + defaultIsLoggedInValue + "')"
            c.execute(user_data)
            # Commit Changes
            conn.commit()

            # Close the connection to the database
            conn.close()

        reset()
        showUserSubmitted = Toplevel()
        showUserSubmitted.geometry("300x300")
        showUserSubmitted.title("Submission")

        Label(showUserSubmitted, text="Registration Successfull").pack()

    def reset():
        user_name.delete(0, 'end')
        password.delete(0, 'end')
        confirm_password.delete(0, 'end')
        first_name.delete(0, 'end')
        last_name.delete(0, 'end')
        zipcode.delete(0, 'end')
        email.delete(0, 'end')
        phone_no.delete(0, 'end')
        ans.delete(0, 'end')
        queNumber.set(options[0])


    register = Toplevel()
    register.title('Register User')
    register.geometry('500x500')

    var = StringVar(register)
    queNumber = StringVar(register)

    # Entries
    user_name = Entry(register, width=30)
    user_name.grid(row=0, column=1, padx=20)
    user_name.focus_set()

    password = Entry(register, width=30, show="*")
    password.grid(row=1, column=1, padx=20)

    confirm_password = Entry(register, width=30, show="*")
    confirm_password.grid(row=2, column=1, padx=20)

    first_name = Entry(register, width=30)
    first_name.grid(row=3, column=1, padx=20)

    last_name = Entry(register, width=30)
    last_name.grid(row=4, column=1, padx=20)

    zipcode = Entry(register, width=30)
    zipcode.grid(row=9, column=1, padx=20)

    email = Entry(register, width=30)
    email.grid(row=10, column=1, padx=20)

    options = ('----None----', 'What was your favorite sport in high school?', "What is your pet's name?",
               "In what year was your father born?",
               "In what year was your mother born?", "In what country where you born?", "What is your favorite movie?",
               "What is your favorite sport?", "What is the name of your hometown?",
               "What was your favourite subject in school?")
    queNumber.set(options[0])
    drop = OptionMenu(register, queNumber, *options)
    drop.grid(row=11, column=1)
    ans = Entry(register, width=30)
    ans.grid(row=12, column=1, padx=20)

    phone_no = Entry(register, width=30)
    phone_no.grid(row=13, column=1, padx=20)

    # Labels
    Label(register, text="Username*").grid(row=0, column=0)
    Label(register, text="Password*").grid(row=1, column=0)
    Label(
        register, text="Confirm Password*").grid(row=2, column=0)
    Label(
        register, text="First Name*").grid(row=3, column=0)
    Label(register, text="Last Name").grid(row=4, column=0)

    radio = Radiobutton(register, text="Male", padx=14, variable=var, value="M").grid(row=6, column=1, sticky="nsew")
    radio = Radiobutton(register, text="Female", padx=14, variable=var, value="F").grid(row=7, column=1, sticky="nsew")
    radio = Radiobutton(register, text="Other", padx=14, variable=var, value="T").grid(row=8, column=1, sticky="nsew")

    Label(register, text='Gender*').grid(row=5, column=0)

    Label(register, text="Pincode*").grid(row=9, column=0)
    Label(register, text="Email*").grid(row=10, column=0)
    Label(
        register, text="Security question*").grid(row=11, column=0)
    Label(register, text="Answer*").grid(row=12, column=0)
    Label(register, text="Phone No*").grid(row=13, column=0)
    Label(
        register, text="All fields marked with (*) are compulsory").place(x=40, y=400)

    # Create Submit Button
    submit_btn = Button(register, text="Register",
                        bg="white", fg="black", height=2, width=20, command=submit)
    submit_btn.place(x=60, y=350)

    reset_btn = Button(register, text="Reset",
                       bg="white", fg="black", height=2, width=20, command=reset)
    reset_btn.place(x=260, y=350)

    # Execute the register GUI
    register.mainloop()


number = []


def login_user():
    def checkUsernamePassword():
        def product_category():

            loginUser.destroy()
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"
            )

            c = conn.cursor()
            c.execute("SELECT * FROM products")
            allRecords = c.fetchall()

            productIDs = list(map(itemgetter(0), allRecords))
            productNames = list(map(itemgetter(1), allRecords))
            productInfo = list(map(itemgetter(2), allRecords))
            productPrice = list(map(itemgetter(3), allRecords))
            productImages = list(map(itemgetter(4), allRecords))
            productCategories = list(map(itemgetter(5), allRecords))
            recordOfItemsInCart1 = []

            def myCart():

                def onFrameConfigure(event):
                    canvas.configure(scrollregion=canvas.bbox("all"))

                myCart1 = Toplevel()
                myCart1.title("View Cart")
                myCart1.geometry("600x600")
                conn1 = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd=.....,
                    database="loginForPython"
                )
                canvas = Canvas(myCart1)
                canvas.grid(sticky=N + S + E + W)

                yscrollbar = Scrollbar(myCart1, command=canvas.yview)
                yscrollbar.grid(row=0, column=3, sticky=N + S)

                canvas.configure(yscrollcommand=yscrollbar.set)

                frame = Frame(canvas)

                canvas.create_window((0, 0), window=frame, anchor='nw')
                frame.bind("<Configure>", onFrameConfigure)
                myCart1.grid_rowconfigure(0, weight=1)
                myCart1.grid_columnconfigure(0, weight=1)

                everyProduct = IntVar()
                sumOfEveryItem = 0
                cur = conn1.cursor()
                cur.execute("SELECT * FROM cartItems where userID=('" + str(username) + "')")
                records = cur.fetchall()
                productIDsInCart = list(map(itemgetter(1), records))
                print(productIDsInCart)

                for item in range(len(productIDsInCart)):
                    sql = "SELECT * FROM products where pid=('" + str(productIDsInCart[item]) + "')"
                    cur.execute(sql)
                    recordOfItemsInCart1.append(cur.fetchone())

                recordOfItemsInCart = list(dict.fromkeys(recordOfItemsInCart1))

                namesOfProductsInCart = list(map(itemgetter(1), recordOfItemsInCart))
                priceOfProductsInCart = list(map(itemgetter(3), recordOfItemsInCart))
                pathOfProductsInCart = list(map(itemgetter(4), recordOfItemsInCart))
                counters = [IntVar() for _ in range(len(namesOfProductsInCart))]
                priceLists = [IntVar() for _ in range(len(namesOfProductsInCart))]

                priceOfEvery = []
                sum1 = 0
                totalPrice = IntVar()
                for i in range(len(namesOfProductsInCart)):
                    counters[i].set(1)
                    sum1 += priceOfProductsInCart[i]
                    sql1 = "UPDATE cartItems set price=('" + str(
                        priceOfProductsInCart[i]) + "') where (userID=('" + str(username) + "') and productID=('" + str(
                        productIDsInCart[i]) + "'))"
                    cur.execute(sql1)
                    conn1.commit()
                totalPrice.set(sum1)

                def increase_stat(event=None, counter=None, mul=None, index=None):
                    counter.set(counter.get() + 1)
                    mul.set(mul.get() + priceOfProductsInCart[index])
                    sql1 = "UPDATE cartItems set quantity=('" + str(counter.get()) + "') where (userID=('" + str(
                        username) + "') and productID=('" + str(productIDsInCart[index]) + "'))"
                    sql2 = "UPDATE cartItems set price=('" + str(mul.get()) + "') where (userID=('" + str(
                        username) + "') and productID=('" + str(productIDsInCart[index]) + "'))"
                    try:
                        cur.execute(sql1)
                        conn1.commit()
                        cur.execute(sql2)
                        conn1.commit()
                    except:
                        MessageBox.showinfo("Error", "Unable to process request SQL")
                        conn1.rollback()

                def decrease_stat(event=None, counter=None, mul=None, index=None):
                    counter.set(counter.get() - 1)
                    mul.set(mul.get() - priceOfProductsInCart[index])
                    sql1 = "UPDATE cartItems set quantity=('" + str(counter.get()) + "') where (userID=('" + str(
                        username) + "') and productID=('" + str(productIDsInCart[index]) + "'))"
                    sql2 = "UPDATE cartItems set price=('" + str(mul.get()) + "') where (userID=('" + str(
                        username) + "') and productID=('" + str(productIDsInCart[index]) + "'))"
                    try:
                        cur.execute(sql1)
                        conn1.commit()
                        cur.execute(sql2)
                        conn1.commit()
                    except:
                        MessageBox.showinfo("Error", "Unable to process request")
                        conn1.rollback()

                def calcPrice():
                    cur.execute("SELECT sum(price) from cartItems where userID=('" + username + "')")
                    rec = cur.fetchone()

                    totalPrice.set(rec[0])

                def checkOut():
                    orderid = randint(10000, 99999)
                    conn2 = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd=.....,
                        database="loginForPython"
                    )
                    c2 = conn2.cursor()
                    sql0 = "SELECT price FROM cartItems where userID=('" + str(username) + "')"
                    c2.execute(sql0)
                    rec1 = c2.fetchall()
                    totalPriceList = list(map(itemgetter(0), rec1))
                    print(totalPriceList)
                    sql2 = "SELECT * FROM showorders"
                    c2.execute(sql2)
                    rec = c2.fetchall()
                    orderIDList = list(map(itemgetter(2), rec))
                    if orderid not in orderIDList:
                        for item in range(len(productIDsInCart)):
                            sql1 = "INSERT INTO showorders(userID, productID, orderID, price) values('" + str(
                                username) + "','" + str(productIDsInCart[item]) + "','" + str(orderid) + "','" + str(
                                totalPriceList[item]) + "')"
                            c2.execute(sql1)
                            conn2.commit()

                        sql3 = "DELETE FROM cartItems where userID=('" + str(username) + "')"
                        c2.execute(sql3)
                        conn2.commit()
                        MessageBox.showinfo("CHECKED OUT",
                                            "Your Order ID is " + str(orderid) + " and yet to be confirmed by admin")
                        conn2.close()
                        conn1.close()
                        myCart1.destroy()
                    else:
                        orderid = randint(10000, 99999)
                        checkOut()

                for i in range(len(namesOfProductsInCart)):
                    priceLists[i].set(priceOfProductsInCart[i])

                row = 1
                Label(frame, text="Image").grid(row=0, column=0)
                Label(frame, text="Name").grid(row=0, column=1)
                Label(frame, text="Quantity").grid(row=0, column=3)
                Label(frame, text="Price").grid(row=0, column=5)
                Button(myCart1, text="BACK", activebackground="gray", activeforeground="white",
                       bg="white", fg="black", command=myCart1.destroy).place(x=505, y=0, width=70, height=35)
                n = 2

                for everyItem in range(len(productIDsInCart)):

                    path = pathOfProductsInCart[everyItem]
                    image = Image.open(path)
                    [imageSizeWidth, imageSizeHeight] = [45, 75]
                    same = True

                    newImageSizeWidth = int(imageSizeWidth * n)
                    if same:
                        newImageSizeHeight = int(imageSizeHeight * n)
                    else:
                        newImageSizeHeight = int(imageSizeHeight / n)

                    image = image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(image)
                    imgCanvas = Label(frame, image=img)
                    imgCanvas.image = img
                    imgCanvas.grid(row=row, column=0, padx=10, pady=10)

                    Label(frame, text=namesOfProductsInCart[everyItem]).grid(row=row, column=1)

                    Label(frame, textvariable=counters[everyItem]).grid(row=row, column=3)
                    Button(frame, text="+", command=lambda counter=counters[everyItem], mul=priceLists[everyItem],
                                                           index=everyItem: increase_stat(counter=counter, index=index,
                                                                                          mul=mul)).grid(row=row,
                                                                                                         column=4)
                    Button(frame, text="-", command=lambda counter=counters[everyItem], mul=priceLists[everyItem],
                                                           index=everyItem: decrease_stat(counter=counter, index=index,
                                                                                          mul=mul)).grid(row=row,
                                                                                                         column=2)
                    priceLabel = Label(frame, textvariable=priceLists[everyItem])
                    priceLabel.grid(row=row, column=5)

                    row += 1
                calcPriceBtn = Button(frame, text="Calculate Price",activebackground="gray", activeforeground="white",
                       bg="white", fg="black",height=2, width=20, command=calcPrice)
                checkOutBtn = Button(frame, text="Check Out",activebackground="gray", activeforeground="white",
                       bg="white", fg="black",height=2, width=20, command=checkOut)
                Label(frame, text="Total", font='Times 16 bold').grid(row=row + 1, column=5)
                totalPriceLabel = Label(frame, textvariable=totalPrice, font='Times 16 bold')
                totalPriceLabel.grid(row=row + 1, column=6)
                calcPriceBtn.grid(row=row, column=5)
                checkOutBtn.grid(row=row + 2, column=5)
                frame.mainloop()
                canvas.configure(scrollregion=canvas.bbox("all"))

            def allCategoryContents(row, x, y, categoryList, category):

                def addToCart():
                    if my_btn['state'] == ACTIVE:
                        my_btn.configure(state=DISABLED, text="Added to the Cart", image=None, compound=CENTER)
                        my_btn.image = None
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd=.....,
                        database="loginForPython"
                    )

                    c = conn.cursor()
                    sql = "INSERT INTO cartItems(userID, productID) values('" + str(username) + "','" + str(
                        productIDs[category]) + "')"
                    try:
                        c.execute(sql)
                        MessageBox.showinfo("Product Added!", "Product Added to the Cart")

                        conn.commit()
                    # print(productIDs)
                    except:
                        MessageBox.showinfo('Error', 'Unable to add product')
                        conn.rollback()
                    finally:
                        conn.close()

                n = 2
                cartBtnPath = "C:/Users/ADMIN/Documents/python prg/Images/CartIcon.ppm"
                path = productImages[category]
                image = Image.open(path)
                [imageSizeWidth, imageSizeHeight] = [45, 75]
                same = True
                newImageSizeWidth = int(imageSizeWidth * n)
                if same:
                    newImageSizeHeight = int(imageSizeHeight * n)
                else:
                    newImageSizeHeight = int(imageSizeHeight / n)

                image = image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(image)
                imgCanvas = Label(categoryList, image=img)
                imgCanvas.image = img
                imgCanvas.grid(row=row, column=0, padx=10, pady=10)

                cartBtnImg1 = Image.open(cartBtnPath)
                cartBtnImg1 = cartBtnImg1.resize((20, 20), Image.ANTIALIAS)

                cartBtnImg = ImageTk.PhotoImage(cartBtnImg1)
                Label(categoryList, text=productNames[category], font="Times 16").grid(row=row, column=1, padx=10,
                                                                                       pady=10)

                my_btn = Button(categoryList, text="Add to Cart", font="Times 14", image=cartBtnImg, compound=LEFT,
                                activebackground="gray", activeforeground="white",
                                bg="white", fg="black",
                                command=addToCart)
                my_btn.image = cartBtnImg

                my_btn.grid(row=row, column=2, padx=10, pady=10)

            def allCategoryMainPage(parentTk, text, categoryNumber):

                def onFrameConfigure(event):
                    canvas.configure(scrollregion=canvas.bbox("all"))

                canvas = Canvas(parentTk)
                canvas.grid(sticky=N + S + E + W)

                yscrollbar = Scrollbar(parentTk, command=canvas.yview)
                yscrollbar.grid(row=0, column=3, sticky=N + S)

                canvas.configure(yscrollcommand=yscrollbar.set)

                frame = Frame(canvas)

                canvas.create_window((0, 0), window=frame, anchor='nw')
                frame.bind("<Configure>", onFrameConfigure)

                parentTk.grid_rowconfigure(0, weight=1)
                parentTk.grid_columnconfigure(0, weight=1)

                cartBtnPath = "C:/Users/ADMIN/Documents/python prg/Images/CartIcon.ppm"
                Label(frame, text=text, font="Times 20").grid(row=0, column=1)
                cartBtnImg1 = Image.open(cartBtnPath)
                cartBtnImg1 = cartBtnImg1.resize((20, 20), Image.ANTIALIAS)
                cartBtnImg = ImageTk.PhotoImage(cartBtnImg1)

                cartContents = Button(frame, text="My Cart", image=cartBtnImg, compound=LEFT, command=myCart,
                                      font="Times 16", activebackground="gray", activeforeground="white",
                                      bg="white", fg="black")
                cartContents.image = cartBtnImg
                cartContents.grid(row=0, column=2)
                row = 1
                x = 0
                y = 0

                for category in range(len(productCategories)):
                    if productCategories[category] == categoryNumber:
                        allCategoryContents(row, x, y, frame, category)
                        row += 1
                        x += 50
                        y += 50
                canvas.configure(scrollregion=canvas.bbox("all"))

            def mobileCategory():
                mobilesList = Toplevel()
                mobilesList.geometry("600x600")
                mobilesList.title("Mobiles")
                allCategoryMainPage(mobilesList, "MOBILES", 6666)
                Button(mobilesList, text="BACK", activebackground="gray", activeforeground="white",
                       bg="white", fg="black", command=mobilesList.destroy).place(x=505, y=0, width=70, height=35)

            def fashionCategory():
                fashionList = Toplevel()
                fashionList.title("Fashion")
                fashionList.geometry("600x600")
                allCategoryMainPage(fashionList, "FASHION", 1111)
                Button(fashionList, text="BACK", activebackground="gray", activeforeground="white",
                       bg="white", fg="black", command=fashionList.destroy).place(x=505, y=0, width=70, height=35)
                fashionList.mainloop()

            def drugCategory():
                drugList = Toplevel()
                drugList.title("Medicines and Drugs")
                drugList.geometry("600x600")
                allCategoryMainPage(drugList, "MEDICINES", 3333)
                Button(drugList, text="BACK", activebackground="gray", activeforeground="white",
                       bg="white", fg="black", command=drugList.destroy).place(x=505, y=0, width=70, height=35)
                drugList.mainloop()

            def elecCategory():
                elecList = Toplevel()
                elecList.title("Electronics")
                elecList.geometry("600x600")
                allCategoryMainPage(elecList, "ELECTRONICS", 2222)
                Button(elecList, text="BACK", activebackground="gray", activeforeground="white",
                       bg="white", fg="black", command=elecList.destroy).place(x=505, y=0, width=70, height=35)
                elecList.mainloop()

            def grocery():
                groceryList = Toplevel()
                groceryList.title("Grocery")
                groceryList.geometry("600x600")
                allCategoryMainPage(groceryList, "GROCERIES", 5555)
                Button(groceryList, text="BACK", activebackground="gray", activeforeground="white",
                       bg="white", fg="black", command=groceryList.destroy).place(x=505, y=0, width=70, height=35)
                groceryList.mainloop()

            def logout_command():
                productCategory.destroy()
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd=.....,
                    database="loginForPython"
                )
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM user_info")
                myresult = mycursor.fetchall()
                logInDetail = 'F'
                mycursor.execute(
                    "UPDATE user_info set isLoggedIn = ('" + logInDetail + "') where user_name=('" + username + "')")
                conn.commit()

                MessageBox.showinfo('Logged Out', 'You have successfully logged out')

            productCategory = Toplevel()
            productCategory.title("Product Category")
            productCategory.geometry("800x800")
            backgroundImg = backgroundImage(productCategory, 800, 800)
            imgCanvas = Label(productCategory, image=backgroundImg)
            imgCanvas.place(x=0, y=0, relwidth=1, relheight=1)

            menubar = Menubutton(
                productCategory, text="---", relief=FLAT, bg="grey", justify=LEFT)
            menubar.place(x=0, y=0)
            menubar.menu = Menu(menubar)
            menubar["menu"] = menubar.menu
            menubar.menu.add_checkbutton(label=username)
            menubar.menu.add_checkbutton(
                label="Logout", command=logout_command)
            menubar.grid(row=0, sticky=W + E)

            mobiles = Button(productCategory, text="Mobiles", bg="bisque2",
                             command=mobileCategory)
            mobiles.place(x=250, y=70, h=40, w=200, anchor=CENTER)

            fashion = Button(productCategory, text="Fashion", bg="bisque2",
                             command=fashionCategory)
            fashion.place(x=250, y=170, h=40, w=200, anchor=CENTER)

            home = Button(productCategory, text="Medicines and Drugs", bg="bisque2", command=drugCategory)
            home.place(x=250, y=270, h=40, w=200, anchor=CENTER)

            toys = Button(productCategory, text="Electronics", bg="bisque2", command=elecCategory)
            toys.place(x=250, y=370, h=40, w=200, anchor=CENTER)

            groceryBtn = Button(productCategory, text="Groceries", bg="bisque2", command=grocery)
            groceryBtn.place(x=250, y=470, h=40, w=200, anchor=CENTER)

            productCategory.mainloop()

        username = username_entry.get()
        password = password_entry.get()
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"
            )
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM user_info")

            myresult = mycursor.fetchall()
            username_list = list(map(itemgetter(0), myresult))
            password_list = list(map(itemgetter(1), myresult))
            isLoggedIn_list = list(map(itemgetter(10), myresult))
            if username in username_list:
                index_of_username = username_list.index(username)

                if password in password_list[index_of_username]:
                    logInDetail = isLoggedIn_list[index_of_username]
                    logInDetail = 'T'
                    username = username_entry.get()
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd=.....,
                        database="loginForPython"
                    )
                    mycursor = conn.cursor()
                    mycursor.execute("SELECT * FROM user_info")

                    myresult = mycursor.fetchall()

                    mycursor.execute(
                        "UPDATE user_info set isLoggedIn = ('" + logInDetail + "') where user_name=('" + username + "')")
                    conn.commit()
                    product_category()

                else:
                    MessageBox.showinfo("Incorrect password",
                                        "Password entered by the user is incorrect")
            else:
                MessageBox.showinfo(
                    "Warning!", "Given username does not exist")
        except Error as e:
            print('MySQL connection is not established', e)
        finally:
            conn.close()

    def forgotPassword():
        def sendOTP():
            username = username_entry.get()
            email = email_id_entry.get()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("write email", .....)
            otpValue = str(randint(1000, 9999))
            msg = "{}".format(otpValue)
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"
            )
            mycursor = conn.cursor(buffered=True)
            mycursor.execute("SELECT * FROM user_info")
            sql = "UPDATE user_info SET otp=('" + otpValue + "') WHERE user_name=('" + username + "')"
            try:
                mycursor.execute(sql)
                conn.commit()
            except Exception as e:
                conn.rollback()
            finally:
                server.sendmail("write email", email, msg)
                server.quit()
                conn.close()

        def update():
            username = username_entry.get()
            email = email_id_entry.get()
            newPassword = new_password_entry.get()
            confirmNewPassword = confirm_password_entry.get()
            otp = otp_entry.get()
            answer = ans.get()
            if newPassword != confirmNewPassword:
                MessageBox.showinfo("Warning!",
                                    "New password and confirm new password does not match")
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd=.....,
                        database="loginForPython"
                    )
                    mycursor = conn.cursor()
                    mycursor.execute("SELECT * FROM user_info")

                    myresult = mycursor.fetchall()
                    username_list = list(map(itemgetter(0), myresult))
                    email_id_list = list(map(itemgetter(6), myresult))
                    answers_list = list(map(itemgetter(8), myresult))
                    otp_list = list(map(itemgetter(11), myresult))

                    if username in username_list:
                        index_of_username = username_list.index(username)
                        if email in email_id_list[index_of_username]:
                            if otp in otp_list[index_of_username]:
                                if answer in answers_list[index_of_username]:
                                    sql = "UPDATE user_info SET password=('" + \
                                          newPassword + \
                                          "') WHERE user_name=('" + username + "')"
                                    try:
                                        mycursor.execute(sql)
                                        conn.commit()
                                    except Error as e:
                                        MessageBox.showinfo(
                                            "Error", "Error while connecting with database")
                                        conn.rollback()
                                else:
                                    MessageBox.showinfo(
                                        "Warning!", "Answer entered is incorrect")
                            else:
                                MessageBox.showinfo(
                                    "Warning!", "OTP entered is incorrect")
                                reset_forgot()
                        else:
                            MessageBox.showinfo("Incorrect email",
                                                "Email id entered by the user is incorrect")
                    else:
                        MessageBox.showinfo(
                            "Warning!", "Given username does not exist")
                except Error as e:
                    print("Error while connecting to database", e)
                finally:
                    conn.close()
            reset_forgot()

        def reset_forgot():
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            new_password_entry.delete(0, 'end')
            confirm_password_entry.delete(0, 'end')
            email_id_entry.delete(0, 'end')
            otp_entry.delete(0, 'end')
            ans.delete(0, 'end')
            queNumber.set(options[0])


        queNumber = StringVar()
        passwordForget = Toplevel()
        passwordForget.title("Forgot Password")
        passwordForget.geometry("300x650")
        Label(passwordForget, text="Username*").pack()
        username_entry = Entry(passwordForget, width=20)
        username_entry.focus_set()
        username_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Email ID*").pack()
        email_id_entry = Entry(passwordForget, width=20)
        email_id_entry.pack()

        Label(passwordForget, text="").pack()
        otp_btn = Button(passwordForget, text='Send OTP', activebackground="gray", activeforeground="white",
                         bg="white", fg="black", height=2, width=20, command=sendOTP)
        otp_btn.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="OTP*").pack()
        otp_entry = Entry(passwordForget, width=20, show='*')
        otp_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="New Password*").pack()
        new_password_entry = Entry(passwordForget, width=20, show='*')
        new_password_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Confirm Password*").pack()
        confirm_password_entry = Entry(passwordForget, width=20, show='*')
        confirm_password_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Security Question*").pack()

        options = ('----None----', 'What was your favorite sport in high school?', "What is your pet's name?",
                   "In what year was your father born?",
                   "In what year was your mother born?", "In what country where you born?",
                   "What is your favorite movie?", "What is your favorite sport?", "What is the name of your hometown?",
                   "What was your favourite subject in school?")
        queNumber.set(options[0])
        drop = OptionMenu(passwordForget, queNumber, *options)
        drop.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Answer*").pack()
        ans = Entry(passwordForget, width=30)
        ans.pack()

        Label(passwordForget, text="").pack()
        update_btn = Button(passwordForget, text='Update', activebackground="gray", activeforeground="white",
                            bg="white", fg="black", height=2, width=20, command=update)
        update_btn.pack()

        Label(passwordForget, text="").pack()
        reset_btn = Button(passwordForget, text="Reset", activebackground="gray", activeforeground="white",
                           bg="white", fg="black", height=2, width=20, command=reset_forgot)
        reset_btn.pack()

    def reset():
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

    loginUser = Toplevel()
    loginUser.title("Login")
    loginUser.geometry("300x300")
    loginUser.bind('<Return>', lambda event: checkUsernamePassword())

    Label(loginUser, text="Please enter login details").pack()
    Label(loginUser, text="").pack()

    username_label = Label(loginUser, text="Username*").pack()
    username_entry = Entry(loginUser, width=20)
    username_entry.focus_set()
    username_entry.pack()

    Label(loginUser, text="").pack()
    password_label = Label(loginUser, text="Password*").pack()
    password_entry = Entry(loginUser, width=20, show='*')
    password_entry.pack()

    Label(loginUser, text="").pack()
    login_button = Button(loginUser, text="Login", width=15,
                          height=1, command=checkUsernamePassword)
    login_button.pack()
    Label(loginUser, text="").pack()
    forgot_password = Button(
        loginUser, text="Forgot Password", width=15, height=1, command=forgotPassword)
    forgot_password.pack()
    Label(loginUser, text="").pack()

    reset_everything = Button(loginUser, text="Reset",
                              width=15, height=1, command=reset)
    reset_everything.pack()
    loginUser.mainloop()


def login_admin():
    def checkUsernamePassword():
        def logout_command():
            logOut = Toplevel()

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"
            )
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM admin_info")
            myresult = mycursor.fetchall()

            logInDetail = 'F'
            mycursor.execute(
                "UPDATE admin_info set isLoggedIn = ('" + logInDetail + "') where admin_id=('" + username + "')")
            conn.commit()

            Label(logOut, text="You have successfully logged out").pack()
            logOut.mainloop()

        username = username_entry.get()
        password = password_entry.get()
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"
            )
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM admin_info")

            myresult = mycursor.fetchall()
            username_list = list(map(itemgetter(0), myresult))
            password_list = list(map(itemgetter(1), myresult))
            isLoggedIn_list = list(map(itemgetter(6), myresult))
            if username in username_list:
                index_of_username = username_list.index(username)

                if password in password_list[index_of_username]:
                    logInDetail = isLoggedIn_list[index_of_username]
                    logInDetail = 'T'
                    username = username_entry.get()
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd=.....,
                        database="loginForPython"
                    )
                    mycursor = conn.cursor()
                    mycursor.execute("SELECT * FROM admin_info")

                    myresult = mycursor.fetchall()

                    mycursor.execute(
                        "UPDATE admin_info set isLoggedIn = ('" + logInDetail + "') where admin_id=('" + username + "')")
                    conn.commit()
                    Login()


                else:
                    MessageBox.showinfo("Incorrect password",
                                        "Password entered by the user is incorrect")
            else:
                MessageBox.showinfo(
                    "Warning!", "Given username does not exist")
        except Error as e:
            print('MySQL connection is not established', e)
        finally:
            conn.close()

    def forgotPassword():
        def sendOTP():
            username = username_entry.get()
            email = email_id_entry.get()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("write email", .....)
            otpValue = str(randint(1000, 9999))
            msg = "{}".format(otpValue)
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"
            )
            mycursor = conn.cursor(buffered=True)
            mycursor.execute("SELECT * FROM admin_info")
            sql = "UPDATE admin_info SET otp=('" + otpValue + "') WHERE admin_id=('" + username + "')"
            try:
                mycursor.execute(sql)
                conn.commit()
            except Exception as e:
                conn.rollback()
            finally:
                server.sendmail("write email", email, msg)
                server.quit()
                conn.close()

        def update():
            username = username_entry.get()
            emailId = email_id_entry.get()
            newPassword = new_password_entry.get()
            confirmNewPassword = confirm_password_entry.get()
            otpValue = otp_entry.get()

            if newPassword != confirmNewPassword:
                MessageBox.showinfo("Warning!",
                                    "New password and confirm new password does not match")
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd=.....,
                        database="loginForPython"
                    )
                    mycursor = conn.cursor()
                    mycursor.execute("SELECT * FROM admin_info")

                    myresult = mycursor.fetchall()
                    username_list = list(map(itemgetter(0), myresult))
                    otp_list = list(map(itemgetter(8), myresult))
                    email_id_list = list(map(itemgetter(7), myresult))

                    if username in username_list:
                        index_of_username = username_list.index(username)
                        if emailId in email_id_list[index_of_username]:
                            if otpValue in otp_list[index_of_username]:
                                sql = "UPDATE admin_info SET password=('" + \
                                      newPassword + \
                                      "') WHERE admin_id=('" + username + "')"
                                try:
                                    mycursor.execute(sql)
                                    conn.commit()
                                except Error as e:
                                    MessageBox.showinfo(
                                        "Error", "Error while connecting with database")
                                    conn.rollback()
                            else:
                                MessageBox.showinfo("Incorrect OTP", "OTP entered by the user is incorrect")
                        else:
                            MessageBox.showinfo("Incorrect email",
                                                "Email ID entered by the user is incorrect")
                    else:
                        MessageBox.showinfo(
                            "Warning!", "Given username does not exist")
                except Error as e:
                    print("Error while connecting to database", e)
                finally:
                    conn.close()
            reset_forgot()

        def reset_forgot():
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            new_password_entry.delete(0, 'end')
            confirm_password_entry.delete(0, 'end')
            otp_entry.delete(0, 'end')
            email_id_entry.delete(0, 'end')
            username_entry.focus_set()

        queNumber = StringVar()
        passwordForget = Toplevel()
        passwordForget.geometry("300x450")
        Label(passwordForget, text="Username*").pack()
        username_entry = Entry(passwordForget, width=20)
        username_entry.focus_set()
        username_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Email ID*").pack()
        email_id_entry = Entry(passwordForget, width=20)
        email_id_entry.pack()

        Label(passwordForget, text="").pack()
        otp_btn = Button(passwordForget, text='Send OTP', command=sendOTP)
        otp_btn.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="OTP*").pack()
        otp_entry = Entry(passwordForget, width=20)
        otp_entry.pack()

        Label(loginAdmin, text="").pack()
        Label(passwordForget, text="New Password*").pack()
        new_password_entry = Entry(passwordForget, width=20, show='*')
        new_password_entry.pack()

        Label(passwordForget, text="").pack()
        Label(passwordForget, text="Confirm Password*").pack()
        confirm_password_entry = Entry(passwordForget, width=20, show='*')
        confirm_password_entry.pack()

        Label(passwordForget, text="").pack()
        update_btn = Button(passwordForget, text='Update', activebackground="gray", activeforeground="white",
                            bg="white", fg="black", height=2, width=20, command=update)
        update_btn.pack()

        Label(passwordForget, text="").pack()
        reset_btn = Button(passwordForget, text="Reset", activebackground="gray", activeforeground="white",
                           bg="white", fg="black", height=2, width=20, command=reset_forgot)
        reset_btn.pack()

    def reset():
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

    def show_details():
        def onFrameConfigure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        detailsUser = Toplevel()
        canvas = Canvas(detailsUser)
        canvas.grid(sticky=N + S + E + W)

        yscrollbar = Scrollbar(detailsUser, command=canvas.yview)
        yscrollbar.grid(row=0, column=3, sticky=N + S)

        canvas.configure(yscrollcommand=yscrollbar.set)

        frame = Frame(canvas)

        canvas.create_window((0, 0), window=frame, anchor='nw')

        frame.bind("<Configure>", onFrameConfigure)

        detailsUser.grid_rowconfigure(0, weight=1)
        detailsUser.grid_columnconfigure(0, weight=1)
        detailsUser.geometry("500x500")

        Label(frame, text="Entries", font="comic 20 bold italic").grid(row=0, column=1)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=.....,
            database="loginForPython"
        )
        c = conn.cursor()
        c.execute("select * from user_info")
        row = 1
        Label(frame, text="Username").grid(row=row, column=0)
        Label(frame, text="Passwords").grid(row=row, column=1)
        Label(frame, text="First Name").grid(row=row, column=2)
        row += 1
        result = c.fetchall()
        usernames = list(map(itemgetter(0), result))
        passwords = list(map(itemgetter(1), result))
        firstNames = list(map(itemgetter(2), result))
        for record in range(len(result)):
            Label(frame, text=usernames[record]).grid(row=row, column=0)
            Label(frame, text=passwords[record]).grid(row=row, column=1)
            Label(frame, text=firstNames[record]).grid(row=row, column=2)
            row += 1

        canvas.configure(scrollregion=canvas.bbox("all"))
        detailsUser.mainloop()

    def modification():
        def viewpendingorder():
            def onFrameConfigure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            p = Toplevel()
            p.geometry("500x500")
            p.title("View pending orders")
            canvas = Canvas(p)
            canvas.grid(sticky=N + S + E + W)

            yscrollbar = Scrollbar(p, command=canvas.yview)
            yscrollbar.grid(row=0, column=4, sticky=N + S)

            canvas.configure(yscrollcommand=yscrollbar.set)
            frame = Frame(canvas)

            canvas.create_window((0, 0), window=frame, anchor='nw')

            frame.bind("<Configure>", onFrameConfigure)
            p.grid_rowconfigure(0, weight=1)
            p.grid_columnconfigure(0, weight=1)

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"

            )
            c = conn.cursor()
            c.execute("select * from showorders where isApproved=('F')")
            result = c.fetchall()
            userID = list(map(itemgetter(0), result))
            productID = list(map(itemgetter(1), result))
            orderID = list(map(itemgetter(2), result))
            price = list(map(itemgetter(3), result))
            Label(frame, text="PENDING ORDERS", font="comic 20 bold italic").grid(row=0, column=1)
            row = 1
            Label(frame, text="Username", font=('Arial',12)).grid(row=row, column=0)
            Label(frame, text="Product ID", font=('Arial',12)).grid(row=row, column=1)
            Label(frame, text="Order ID", font=('Arial',12)).grid(row=row, column=2)
            Label(frame, text="Price", font=('Arial',12)).grid(row=row, column=4)
            row += 1
            for record in range(len(result)):
                Label(frame, text=userID[record]).grid(row=row, column=0)
                Label(frame, text=productID[record]).grid(row=row, column=1)
                Label(frame, text=orderID[record]).grid(row=row, column=2)
                Label(frame, text=price[record]).grid(row=row, column=3)
                row += 1
            canvas.configure(scrollregion=canvas.bbox("all"))
            p.mainloop()

        def viewcompleteorder():
            def onFrameConfigure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            s = Toplevel()
            s.geometry("500x500")
            s.title("View completed orders")
            canvas = Canvas(s)
            canvas.grid(sticky=N + S + E + W)

            yscrollbar = Scrollbar(s, command=canvas.yview)
            yscrollbar.grid(row=0, column=4, sticky=N + S)

            canvas.configure(yscrollcommand=yscrollbar.set)

            frame = Frame(canvas)

            canvas.create_window((0, 0), window=frame, anchor='nw')

            frame.bind("<Configure>", onFrameConfigure)
            s.grid_rowconfigure(0, weight=1)
            s.grid_columnconfigure(0, weight=1)

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"

            )
            c = conn.cursor()
            c.execute("select * from showorders where isApproved=('T')")
            result = c.fetchall()
            userID = list(map(itemgetter(0), result))
            productID = list(map(itemgetter(1), result))
            orderID = list(map(itemgetter(2), result))
            price = list(map(itemgetter(3), result))
            Label(frame, text="COMPLETED ORDERS", font="comic 20 bold italic").grid(row=0, column=1)
            row = 1
            Label(frame, text="Username",font=('Arial',12)).grid(row=row, column=0)
            Label(frame, text="Product ID",font=('Arial',12)).grid(row=row, column=1)
            #Label(frame, text="Product Name", font=('Arial', 12)).grid(row=row, column=2)
            Label(frame, text="Order ID",font=('Arial',12)).grid(row=row, column=2)
            Label(frame, text="Price",font=('Arial',12)).grid(row=row, column=3)
            row += 1
            for record in range(len(result)):
                Label(frame, text=userID[record]).grid(row=row, column=0)
                Label(frame, text=productID[record]).grid(row=row, column=1)
                Label(frame, text=orderID[record]).grid(row=row, column=2)
                Label(frame, text=price[record]).grid(row=row, column=3)
                row += 1
            canvas.configure(scrollregion=canvas.bbox("all"))
            s.mainloop()

        m = Toplevel()
        m.geometry("300x300")
        pending = Button(m, text="VIEW PENDING ORDERS", activebackground="gray", activeforeground="white",
                         bg="white", fg="black", height=2, width=20, command=viewpendingorder)
        pending.place(x=150, y=80, anchor=CENTER)
        confirm = Button(m, text="VIEW FINAL ORDERS", activebackground="gray", activeforeground="white",
                         bg="white", fg="black", height=2, width=20, command=viewcompleteorder)
        confirm.place(x=150, y=150, anchor=CENTER)
        m.mainloop()

    def update1():
        def deleteorder():
           
            orderID = orderID_entry.get()
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"

            )
            c = conn.cursor()
            c.execute("select * from showorders")
            all_records = c.fetchall()
            orderList = list(map(itemgetter(2), all_records))
            if str(orderID) in str(orderList):
                sql = "delete from showorders where orderID =('" + str(orderID) + "')"
                try:
                    c.execute(sql)
                    conn.commit()
                    MessageBox.showinfo("Success", "Order is cancelled")
                except:
                    conn.rollback()
                finally:
                    conn.close()
            else:
                MessageBox.showinfo("Order id is not present in the database")
           

        def confirm_order():
            
            orderID1 = orderID_entry.get()
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=.....,
                database="loginForPython"

            )
            c = conn.cursor()
            c.execute("select * from showorders")
            res = c.fetchall()
            confirmlist = list(map(itemgetter(2), res))

            if str(orderID1) in str(confirmlist):
                sql = "UPDATE showorders SET isApproved =('T') WHERE orderID =('" + str(orderID1) + "')"
                sql1 = "select email from user_info where user_name in (select s.userID from showorders as s where s.orderID in (select o.orderID from showorders as o where o.isApproved='T'))"

                try:
                    c.execute(sql)

                    conn.commit()
                    c.execute(sql1)
                    rec1 = c.fetchall()
                    emailList = list(map(itemgetter(0), rec1))
                    email = emailList[0]

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login("write email", .....)

                    msg = "Your order ID number " + str(orderID1) + " is confirmed "
                    server.sendmail("write email", email, msg)
                    server.quit()
                    MessageBox.showinfo("Success", "order confirmed")
                except:
                    conn.rollback()
                finally:
                    conn.close()
            else:
                MessageBox.showinfo("Error", "orderid is not present in the database")
           

        m = Toplevel()
        m.geometry("300x300")
        m.title("Order Confirmation")
        Label(m, text="Order ID:", font="comic 20 bold").place(x=10, y=0)
        orderID_entry = Entry(m, width=25)
        orderID_entry.place(x=10, y=35)
        orderID_entry.focus_set()
        final_btn = Button(m, text="CONFIRM ORDER", activebackground="gray", activeforeground="white",
                           width=15, height=2, bg="white", fg="black", command=confirm_order)
        final_btn.place(x=25, y=100)

        delete_btn = Button(m, text="DELETE ORDER", activebackground="gray", activeforeground="white",
                            width=15, height=2, bg="white", fg="black", command=deleteorder)
        delete_btn.place(x=155, y=100)

        m.mainloop()

    def Login():
        MessageBox.askquestion("Confirm", "Are u sure to visit that page")
        Afterlogin = Toplevel()
        Afterlogin.title("Admin")
        Afterlogin.geometry("500x500")
        Label(Afterlogin, text="Administrator work", font="comic 20 bold italic").place(x=250, y=20, anchor=CENTER)

        show_btn = Button(Afterlogin, text="SHOW LOGINS", bg="white", fg="black", height=2, width=20,
                          command=show_details)
        show_btn.place(x=250, y=100, anchor=CENTER)
        updt_btn = Button(Afterlogin, text="MODIFY ORDERS", bg="white", fg="black", height=2, width=20, command=update1)
        updt_btn.place(x=250, y=200, anchor=CENTER)
        vieworder_btn = Button(Afterlogin, text="VIEW ORDERS", bg="white", fg="black", height=2, width=20,
                               command=modification)
        vieworder_btn.place(x=250, y=300, anchor=CENTER)

    loginAdmin = Toplevel()
    loginAdmin.title("Login")
    loginAdmin.geometry("300x300")
    loginAdmin.bind('<Return>', lambda event: checkUsernamePassword())

    Label(loginAdmin, text="Please enter login details").pack()
    Label(loginAdmin, text="").pack()

    username_label = Label(loginAdmin, text="Username*").pack()
    username_entry = Entry(loginAdmin, width=20)
    username_entry.focus_set()
    username_entry.pack()

    Label(loginAdmin, text="").pack()
    password_label = Label(loginAdmin, text="Password*").pack()
    password_entry = Entry(loginAdmin, width=20, show='*')
    password_entry.pack()

    Label(loginAdmin, text="").pack()
    login_button = Button(loginAdmin, text="Login", width=15,
                          height=1, command=checkUsernamePassword)
    login_button.pack()

    Label(loginAdmin, text="").pack()
    forgot_password = Button(
        loginAdmin, text="Forgot Password", width=15, height=1, command=forgotPassword)
    forgot_password.pack()
    Label(loginAdmin, text="").pack()

    reset_everything = Button(loginAdmin, text="Reset",
                              width=15, height=1, command=reset)
    reset_everything.pack()
    loginAdmin.mainloop()


def main_screen():
    global appm
    appm = Tk()
    appm.title("Shopping Cart")
    #appm.iconbitmap('Graphicloads-Colorful-Long-Shadow-Cart.ico')
    # appm.state('zoomed')
    w = 1000
    h = 700
    ws = appm.winfo_screenwidth()
    hs = appm.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    appm.geometry('%dx%d+%d+%d' % (w, h, x, y))

    image = Image.open("ShoppingCart.png")
    photo = ImageTk.PhotoImage(image)

    # Now i want to add photo as a label
    a_label = Label(image=photo)
    a_label.pack()

    title = Message( text='Shopping Cart', width=400, font=("Arial",24,"bold italic"), bg="white", relief=SOLID, borderwidth=2)
    title.place(x=360, y=20)
    login_for_admin = Button(appm, text="Login as Admin",font=('Arial',13,'italic'), fg="black", bg="#22e6df", command=login_admin)
    login_for_admin.place(x=225, y=225, height=50, width=250)

    login_for_user = Button(appm, text="Login as User",font=('Arial',13,'italic'), fg="black", bg="#22e6df", command=login_user)
    login_for_user.place(x=525, y=225, height=50, width=250)

    register_for_user = Button(appm, text="New User ?  Sign up here !", font=('Arial',13,'italic'), fg="black", bg="#22e6df", command=registerUser)
    register_for_user.place(x=375, y=360, width=250, height=50)

    appm.mainloop()


main_screen()
