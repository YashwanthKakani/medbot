from flask import Flask, render_template, redirect, url_for
import mysql.connector
import webbrowser

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Super@30",
    "database": "Medic",
}
cursor=db_config.cursor()
# Home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webcam-access', methods=['GET', 'POST'])
def webcam_access():
    try:
        quantity = None
        if request.method == 'POST':
            quantity = int(request.form['quantity'])  # Get quantity from the form

        while True:
            ret, frame = cap.read()
            barcodes = decode(frame)

            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')

                # Check if the scanned barcode is in the medicine_data dictionary
                if barcode_data in medicine_data:
                    cursor.execute("select * from medicine where sno=%s",(barcode_data,))                                          #executing the command in mysql database
	            data=cursor.fetchone()                                                       
		    a,b,c,d,e,f,g,h,i=data                                                                              #unpacking data tuple
                    if quantity is not None and quantity > 0:
                        # Your inp5==1 logic for adding to cart here
                        if quantity <= e:
                            e -= quantity  # Deduct the quantity from available stock
			    cursor.execute("UPDATE medicine SET Quantity={} where sno={}".format(e,barcode_data))       #updating the quantity in database 
                            mycon.commit()
                            return f"Added {quantity} {b} to cart."
                        else:
                            return "Out of stock."
                    else:
                        return "Invalid quantity."

            cv2.imshow("Webcam Stream", frame)

            # Press 'q' to exit the webcam stream
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        return "Scanning completed."

    except Exception as e:
        return str(e)



@app.route('/page2')
def page2():
    return render_template('page 2.html')

# Route for handling Expired Stock

# Route for handling Expired Stock
@app.route('/expired')
def expired():
    try:
        # Connect to the MySQL database
        db_connection = mysql.connector.connect(**db_config)

        # Create a cursor object to interact with the database
        cursor = db_connection.cursor()

        # Execute a SQL query to retrieve data
        query = "SELECT Sno, Name, Exp_Date, Quantity FROM medicine where exp_date<curdate()"
        cursor.execute(query)

        # Fetch all the rows as a list of tuples
        data = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        db_connection.close()

        # Start building the HTML table structure with CSS styles
        table_html = "<table style='border-collapse: collapse; width: 100%; text-align: center;'>"

        # Add table headers with CSS styles
        table_html += "<thead style='background-color: #125688; color: white;'>"
        for description in cursor.description:
            table_html += f"<th style='padding: 10px;'>{description[0]}</th>"
        table_html += "</thead>"

        # Add table body with CSS styles
        table_html += "<tbody>"
        for row in data:
            table_html += "<tr>"
            for cell in row:
                table_html += f"<td style='padding: 10px; border: 1px solid #ddd;'>{cell}</td>"
            table_html += "</tr>"
        table_html += "</tbody>"

        # Close the HTML table
        table_html += "</table>"

        # Add a heading
        heading_html = "<h1>Expired Medicine</h1>"

        # Add the Instagram-style back button below the table
        back_button_html = (
            "<a href='/' style='text-decoration: none; background-color: #125688; color: white; "
            "padding: 10px 20px; border-radius: 5px; display: block; text-align: center; "
            "margin: 20px auto; width: fit-content;'>Back</a>"
        )

        # Combine the heading, back button, and table HTML
        full_html = heading_html + table_html + back_button_html

        # Return the combined HTML as a response
        return full_html

    except Exception as e:
        return str(e)

# Route for handling Expired Stock
@app.route('/display-sql-table')
def display_sql_table():
    try:
        # Connect to the MySQL database
        db_connection = mysql.connector.connect(**db_config)

        # Create a cursor object to interact with the database
        cursor = db_connection.cursor()

        # Execute a SQL query to retrieve data
        query = "SELECT Sno, Name, Exp_Date, Price, Quantity, Units FROM medicine"
        cursor.execute(query)

        # Fetch all the rows as a list of tuples
        data = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        db_connection.close()

        # Start building the HTML table structure with CSS styles
        table_html = "<table style='border-collapse: collapse; width: 100%; text-align: center;'>"

        # Add table headers with CSS styles
        table_html += "<thead style='background-color: #125688; color: white;'>"
        for description in cursor.description:
            table_html += f"<th style='padding: 10px;'>{description[0]}</th>"
        table_html += "</thead>"

        # Add table body with CSS styles
        table_html += "<tbody>"
        for row in data:
            table_html += "<tr>"
            for cell in row:
                table_html += f"<td style='padding: 10px; border: 1px solid #ddd;'>{cell}</td>"
            table_html += "</tr>"
        table_html += "</tbody>"

        # Close the HTML table
        table_html += "</table>"

        # Add a heading
        heading_html = "<h1>Stock Available</h1>"

        # Add the Instagram-style back button below the table
        back_button_html = (
            "<a href='/' style='text-decoration: none; background-color: #125688; color: white; "
            "padding: 10px 20px; border-radius: 5px; display: block; text-align: center; "
            "margin: 20px auto; width: fit-content;'>Back</a>"
        )

        # Combine the heading, back button, and table HTML
        full_html = heading_html + table_html + back_button_html

        # Return the combined HTML as a response
        return full_html

    except Exception as e:
        return str(e)
if __name__ == '__main__':
    app.run(debug=True)
