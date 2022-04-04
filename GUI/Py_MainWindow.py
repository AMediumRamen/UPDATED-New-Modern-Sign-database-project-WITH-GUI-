from msilib.schema import Error
from optparse import Values
from sqlite3 import Cursor
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from matplotlib.pyplot import show
from PyQt5 import QtWidgets
from Ui_MainWindow import Ui_MainWindow
import pyodbc

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        conn = pyodbc.connect('Driver={ODBC DRIVER 17 for SQL server};'
                      'Server=LAPTOP-0H06NGKU\MSSQLSERVER01;'
                      'Database=test1;'
                      'Trusted_Connection=yes;')
        self.cursor = conn.cursor()



        #SET STARTING WIDGET TO Home_Page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home_page)




        #WHAT CLICKING EACH BUTTON WILL DO (CALL FUNCTION BELOW)
        self.ui.Add_button.clicked.connect(self.showAdd)
        self.ui.Contractor_button.clicked.connect(self.showContractor)
        self.ui.Country_button.clicked.connect(self.showCountry)
        self.ui.Customer_button.clicked.connect(self.showCustomer)
        self.ui.Delete_button.clicked.connect(self.showDelete)
        self.ui.Designer_button.clicked.connect(self.showDesigner)
        self.ui.Driver_button.clicked.connect(self.showDriver)
        self.ui.Employee_button.clicked.connect(self.showEmployee)
        self.ui.Fabricator_button.clicked.connect(self.showFabricator)
        self.ui.HOA_button.clicked.connect(self.showHOA)
        self.ui.Home_button.clicked.connect(self.showHome)
        self.ui.InstallationAddr_button.clicked.connect(self.showInstallationAddr)
        self.ui.Installation_button.clicked.connect(self.showInstallation)
        self.ui.Material_button.clicked.connect(self.showMaterial)
        self.ui.Order_button.clicked.connect(self.showOrder)
        self.ui.Associative_button.clicked.connect(self.showPRMA)
        self.ui.Payment_button.clicked.connect(self.showPayment)
        self.ui.Permi_button.clicked.connect(self.showPermit)
        self.ui.Production_button.clicked.connect(self.showProduction)
        self.ui.State_button.clicked.connect(self.showState)
        self.ui.Supplier_button.clicked.connect(self.showSupplier)
        self.ui.Update_button.clicked.connect(self.showUpdate)
        self.ui.Vehicle_button.clicked.connect(self.showVehicle)
        self.ui.Welder_button.clicked.connect(self.showWelder)

        #LOAD DATA BUTTONS (FUNCTIONS BELOW)
        self.ui.LoadContractorButton.clicked.connect(self.loadContractor)
        self.ui.LoadCountryButton.clicked.connect(self.loadCountry)
        self.ui.LoadCustomerButton.clicked.connect(self.loadCustomer)
        self.ui.LoadDesignerButton.clicked.connect(self.loadDesigner)
        self.ui.LoadDriverButton.clicked.connect(self.loadDriver)
        self.ui.LoadEmployeeButton.clicked.connect(self.loadEmployee)
        self.ui.LoadFabricatorButton.clicked.connect(self.loadFabricator)
        self.ui.LoadHOAButton.clicked.connect(self.loadHOA)
        self.ui.LoadInstallationAddrButton.clicked.connect(self.loadInstallationAddr)
        self.ui.LoadInstallationButton.clicked.connect(self.loadInstallation)
        self.ui.LoadMaterialButton.clicked.connect(self.loadMaterial)
        self.ui.LoadOrderButton.clicked.connect(self.loadOrder)
        self.ui.LoadPRMAButton.clicked.connect(self.loadPRMA)
        self.ui.LoadPaymentButton.clicked.connect(self.loadPayment)
        self.ui.LoadPermitButton.clicked.connect(self.loadPermit)
        self.ui.LoadProductionButton.clicked.connect(self.loadProduction)
        self.ui.LoadStateButton.clicked.connect(self.loadState)
        self.ui.LoadSupplierButton.clicked.connect(self.loadSupplier)
        self.ui.LoadVehicleButton.clicked.connect(self.loadVehicle)
        self.ui.LoadWelderButton.clicked.connect(self.loadWelder)




        #MODIFYING DATA BUTTONS
        self.ui.InsertDataButton.clicked.connect(self.addData)
        self.ui.UpdateDataButton.clicked.connect(self.updateData)



    

    def show(self):
        self.main_win.show()

    #ACTUAL FUNCTIONS TO CHANGE PAGE
    def showAdd(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Add_page)

    def showContractor(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Contractor_page)
    
    def showCountry(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Country_page)

    def showCustomer(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Customer_page)

    def showDelete(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Delete_page)

    def showDesigner(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Designer_page)

    def showDriver(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Driver_page)

    def showEmployee(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Employee_page)

    def showFabricator(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Fabricator_page)

    def showHOA(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.HOA_page)

    def showHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home_page)
        
    def showInstallationAddr(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.InstallationAddr_page)

    def showInstallation(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Installation_page)

    def showMaterial(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Material_page)

    def showOrder(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Order_page)

    def showPRMA(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PRMA_page)

    def showPayment(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Payment_page)

    def showPermit(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Permit_page)

    def showProduction(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Production_page)

    def showState(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.State_page)

    def showSupplier(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Supplier_page)

    def showUpdate(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Update_page)

    def showVehicle(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Vehicle_page)
        
    def showWelder(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Welder_page)





    #LOAD DATA INTO SPECIFIC TABLES WITHIN RESPECTIVE PAGES
    def loadContractor(self):
        result = self.cursor.execute("SELECT * FROM Contractor")
        self.ui.ContractorTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.ContractorTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.ContractorTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        

    def loadCountry(self):
        result = self.cursor.execute("SELECT * FROM Country")
        self.ui.CountryTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.CountryTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.CountryTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        


    def loadCustomer(self):
        result = self.cursor.execute("SELECT * FROM Customer")
        self.ui.CustomerTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.CustomerTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.CustomerTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        

    def loadDesigner(self):
        result = self.cursor.execute("SELECT * FROM Designer")
        self.ui.DesignerTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.DesignerTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.DesignerTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
    

    def loadDriver(self):
        result = self.cursor.execute("SELECT * FROM Driver")
        self.ui.DriverTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.DriverTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.DriverTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        
    def loadEmployee(self):
        result = self.cursor.execute("SELECT * FROM Employee")
        self.ui.EmployeeTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.EmployeeTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.EmployeeTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        
    
    def loadFabricator(self):
        result = self.cursor.execute("SELECT * FROM Fabricator")
        self.ui.FabricatorTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.FabricatorTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.FabricatorTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        

    def loadHOA(self):
        result = self.cursor.execute("SELECT * FROM HOA_ARC")
        self.ui.HOATable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.HOATable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.HOATable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        

    def loadInstallationAddr(self):
        result = self.cursor.execute("SELECT * FROM Installation Address")
        self.ui.InstallationAddrTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.InstallationAddrTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.InstallationAddrTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        
    
    def loadInstallation(self):
        result = self.cursor.execute("SELECT * FROM Installation")
        self.ui.InstallationTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.InstallationTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.InstallationTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        

    def loadMaterial(self):
        result = self.cursor.execute("SELECT * FROM Material")
        self.ui.MaterialTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.MaterialTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.MaterialTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        
    
    def loadOrder(self):
        result = self.cursor.execute("SELECT * FROM [dbo].[Order]")
        self.ui.OrderTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.OrderTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.OrderTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        
    
    def loadPRMA(self):
        result = self.cursor.execute("SELECT * FROM Material_Product")
        self.ui.PRMATable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.PRMATable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.PRMATable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        
    
    def loadPayment(self):
        result = self.cursor.execute("SELECT * FROM Payment")
        self.ui.PaymentTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.PaymentTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.PaymentTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        
    
    def loadPermit(self):
        result = self.cursor.execute("SELECT * FROM Permit")
        self.ui.PermitTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.PermitTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.PermitTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
    

    def loadProduction(self):
        result = self.cursor.execute("SELECT * FROM Production")
        self.ui.ProductionTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.ProductionTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.ProductionTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        

    def loadState(self):
        result = self.cursor.execute("SELECT * FROM State")
        self.ui.StateTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.StateTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.StateTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
       
    
    def loadSupplier(self):
        result = self.cursor.execute("SELECT * FROM Supplier")
        self.ui.SupplierTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.SupplierTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.SupplierTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        
    
    def loadVehicle(self):
        result = self.cursor.execute("SELECT * FROM Vehicle")
        self.ui.VehicleTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.VehicleTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.VehicleTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        
    
    def loadWelder(self):
        result = self.cursor.execute("SELECT * FROM Welder")
        self.ui.WelderTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.WelderTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.WelderTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))





    #MODIFYING DATA FUNCTIONS

    def addData(self):
        tableName = self.ui.TableNameLineEdit.text()
        Values = self.ui.ValuesLineEdit.text()

        self.cursor.execute(("INSERT INTO %s VALUES %s")%(tableName,Values))
        self.ui.AddPageMessage.setText("SUCCESS!")
        self.cursor.commit()

    def updateData(self):
        tableName =self.ui.TableNameLineEditUpdate.text()
        setClause = self.ui.SetLineEdit.text()
        toWhat =self.ui.ToWhatLineEdit.text()
        where = self.ui.WhereLineEdit.text()

        self.cursor.execute("UPDATE %s SET %s = '%s' WHERE %s;"%(tableName,setClause,toWhat,where))
        
        self.ui.UpdateMessageLabel.setText("SUCCESS")
        self.cursor.commit()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

        

