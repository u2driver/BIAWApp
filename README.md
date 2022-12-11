# BIAWApp
Purpose of application:
     Brain Injury Advocates of Wyoming (BIAW) maintains an inventory of durable medical equipment available for loan to the public. This app provides the capability to manage Loan Closet inventory and to manage the process of loaning the equipment.   

User capabilities:
     The app is built with two databases (tables); one for the equipment (‘Equipment’), and one for loan transactions (‘Loans’).  The front end of the application displays scrolling tables of each database.  Each has hyperlinks for entering records, updating records, and deleting records.   Each also includes a hyperlink that displays the corresponding record (s) in the other database.  The Equipment database display has a column that indicates “Available’ or ‘Checked Out’.  If ‘Checked Out’, the field is displayed as a hyperlink to the corresponding loan transaction record that includes the information on the client who has checked it out.  Similarly, the ‘Equp_ID’ field in each loan transaction record is a hyperlink to the corresponding record in the Equipment database that includes details on the specific piece of equipment that was loaned.  
