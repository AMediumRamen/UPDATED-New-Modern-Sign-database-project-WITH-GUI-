
from http import server
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from matplotlib.pyplot import show, table
from PyQt5 import QtWidgets
from Ui_MainWindow import Ui_MainWindow
import pyodbc

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # conn = pyodbc.connect('Driver={ODBC DRIVER 17 for SQL server};'
        #               'Server=LAPTOP-0H06NGKU\MSSQLSERVER01;'
        #               'Database=Test2;'
        #               'Trusted_Connection=yes;')
        # self.cursor = conn.cursor()


        #POPULATING HOME PAGE DROP DOWN LIST
        self.ui.AlterDataDropDown.addItem("Add")
        self.ui.AlterDataDropDown.addItem("Update")
        self.ui.AlterDataDropDown.addItem("Delete")

        #DROP DOWN ACTIVATION
        self.ui.AlterDataDropDown.currentTextChanged.connect(self.dropDownActivate)


    
            




        #SET STARTING WIDGET TO Home_Page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Connection_page)




        #WHAT CLICKING EACH BUTTON WILL DO (CALL FUNCTION BELOW)
        # self.ui.Add_button.clicked.connect(self.showAdd)
        self.ui.Contractor_button.clicked.connect(self.showContractor)
        self.ui.Country_button.clicked.connect(self.showCountry)
        self.ui.Customer_button.clicked.connect(self.showCustomer)
        # self.ui.Delete_button.clicked.connect(self.showDelete)
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
        # self.ui.Update_button.clicked.connect(self.showUpdate)
        self.ui.Vehicle_button.clicked.connect(self.showVehicle)
        self.ui.Welder_button.clicked.connect(self.showWelder)
        self.ui.JOIN_button.clicked.connect(self.showJOIN)
        self.ui.Connection_button.clicked.connect(self.showConnection)

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
        self.ui.DeleteDataButton.clicked.connect(self.deleteData)
        self.ui.pushButton.clicked.connect(self.connection)


        #JOIN PAGE BUTTONS
        self.ui.NotAtWorkFabricator.clicked.connect(self.loadNotAtWorkFabricator)
        self.ui.NotAtWorkWelder.clicked.connect(self.loadNotAtWorkWelder)
        self.ui.NotAtWorkContractor.clicked.connect(self.loadNotAtWorkContractor)
        self.ui.NotAtWorkDesigner.clicked.connect(self.loadNotAtWorkDesigner)
        self.ui.NotAtWorkDriver.clicked.connect(self.loadNotAtWorkDriver)
        self.ui.AtWorkFabricator.clicked.connect(self.loadAtWorkFabricator)
        self.ui.AtWorkWelder.clicked.connect(self.loadAtWorkWelder)
        self.ui.AtWorkContractor.clicked.connect(self.loadAtWorkContractor)
        self.ui.AtWorkDesigner.clicked.connect(self.loadAtWorkDesigner)
        self.ui.AtWorkDriver.clicked.connect(self.loadAtWorkDriver)
        self.ui.AddressInfo.clicked.connect(self.loadAddressInfo)
        self.ui.ProjectedInstallDate.clicked.connect(self.loadProjectedInstallationDate)
        self.ui.InstalledOrders.clicked.connect(self.loadInstalledOrders)
        self.ui.OrderPermitInfo.clicked.connect(self.loadOrderPermitInfo)
        self.ui.OrderHOAInfo.clicked.connect(self.loadOrderHOAInfo)
        self.ui.OrderCustomerInfo.clicked.connect(self.loadOrderCustomerInfo)
        self.ui.OrderPaymentMethod.clicked.connect(self.loadOrderPaymentMethod)
        self.ui.PaidOrder.clicked.connect(self.loadPaidOrder)
        self.ui.CompletedProduction.clicked.connect(self.loadCompletedProduction)
        self.ui.MaterialToSupplier.clicked.connect(self.loadMaterialSupplier)





    
    def show(self):
        self.main_win.show()




    #ACTUAL FUNCTIONS TO CHANGE PAGE    

    def dropDownActivate(self,changeTo):
        if changeTo == "Add":
            self.ui.AlterDataDropDown.activated.connect(self.showAdd)
        elif changeTo == "Update":
            self.ui.AlterDataDropDown.activated.connect(self.showUpdate)
        elif changeTo == "Delete":
            self.ui.AlterDataDropDown.activated.connect(self.showDelete)


    
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
    
    def showJOIN(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.JOIN_page)

    def showConnection(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Connection_page)




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
        result = self.cursor.execute("SELECT * FROM [dbo].[Installation_Address]")
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








    # JOIN PAGE FUNCTIONS
    def loadNotAtWorkFabricator(self):
        result = self.cursor.execute("SELECT Employee.Employee_ID, Fabricator.LastName,Fabricator.FirstName FROM Employee INNER JOIN Fabricator ON Employee.Employee_ID = Fabricator.Employee_ID WHERE AssignedToJob = 0")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))


    def loadNotAtWorkWelder(self):
        result = self.cursor.execute("SELECT Employee.Employee_ID, [dbo].[Welder].LastName,[dbo].[Welder].FirstName FROM Employee INNER JOIN [dbo].[Welder] ON Employee.Employee_ID = [dbo].[Welder].Employee_ID WHERE AssignedToJob = 0")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))

    
    def loadNotAtWorkContractor(self):
        result = self.cursor.execute("SELECT Employee.Employee_ID, Contractor.LastName,Contractor.FirstName FROM Employee INNER JOIN Contractor ON Employee.Employee_ID = Contractor.Employee_ID WHERE AssignedToJob = 0")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))


    def loadNotAtWorkDesigner(self):
        result = self.cursor.execute("SELECT Employee.Employee_ID, Designer.LastName,Designer.FirstName FROM Employee INNER JOIN Designer ON Employee.Employee_ID = Designer.Employee_ID WHERE AssignedToJob = 0")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))

    def loadNotAtWorkDriver(self):
        result = self.cursor.execute("SELECT Employee.Employee_ID, Driver.LastName,Driver.FirstName FROM Employee INNER JOIN Driver ON Employee.Employee_ID = Driver.Employee_ID WHERE AssignedToJob = 0")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))


    def loadAtWorkFabricator(self):
        result = self.cursor.execute("SELECT Employee.Employee_ID, Fabricator.LastName,Fabricator.FirstName FROM Employee INNER JOIN Fabricator ON Employee.Employee_ID = Fabricator.Employee_ID WHERE AssignedToJob = 1")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
    

    def loadAtWorkWelder(self):
        result = self.cursor.execute("SELECT Employee.Employee_ID, [dbo].[Welder].LastName,[dbo].[Welder].FirstName FROM Employee INNER JOIN [dbo].[Welder] ON Employee.Employee_ID = [dbo].[Welder].Employee_ID WHERE AssignedToJob = 1")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))

    def loadAtWorkContractor(self):
        result = self.cursor.execute("SELECT Employee.Employee_ID, Contractor.LastName,Contractor.FirstName FROM Employee INNER JOIN Contractor ON Employee.Employee_ID = Contractor.Employee_ID WHERE AssignedToJob = 1")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))

    def loadAtWorkDesigner(self):
        result = self.cursor.execute("SELECT Employee.Employee_ID, Designer.LastName,Designer.FirstName FROM Employee INNER JOIN Designer ON Employee.Employee_ID = Designer.Employee_ID WHERE AssignedToJob = 1")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))

    def loadAtWorkDriver(self):
        result = self.cursor.execute("SELECT Employee.Employee_ID, Driver.LastName,Driver.FirstName FROM Employee INNER JOIN Driver ON Employee.Employee_ID = Driver.Employee_ID WHERE AssignedToJob = 1")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))


    def loadAddressInfo(self):
        result = self.cursor.execute("SELECT Installation.Installation_ID, [Installation_Address].InstallationAddress_ID,[Installation_Address].AddressLine1,[Installation_Address].AddressLine2,[Installation_Address].ZipCode,[Installation_Address].City FROM Installation Right Join [Installation_Address] ON Installation.InstallationAddress_ID = [Installation_Address].InstallationAddress_ID")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
    


    def loadProjectedInstallationDate(self):
        result = self.cursor.execute("SELECT [dbo].[Order].Order_ID, Installation.Installation_ID, Installation.ProjectedInstallationDate FROM [dbo].[Order] Inner Join Installation ON [dbo].[Order].Installation_ID = Installation.Installation_ID ORDER BY ProjectedInstallationDate")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))


    def loadInstalledOrders(self):
        result = self.cursor.execute("SELECT [dbo].[Order].Order_ID, Installation.Installation_ID, Installation.ActualInstallationDate FROM [dbo].[Order] Inner Join Installation ON [dbo].[Order].Installation_ID = Installation.Installation_ID")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))


    def loadOrderPermitInfo(self):
        result = self.cursor.execute("SELECT [dbo].[Order].Order_ID,Permit.Permit_ID,Permit.PermitExpDate,Permit.[Date Received] FROM [dbo].[Order] Inner Join Permit ON [dbo].[Order].Permit_ID = Permit.Permit_ID ORDER BY [Date Received]")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))


    def loadOrderHOAInfo(self):
        result = self.cursor.execute("SELECT [dbo].[Order].Order_ID,[HOA_ARC].HOAARC_ID, [HOA_ARC].[HOAARC Name], [HOA_ARC].[HOAARC Address], [HOA_ARC].[HOA Phone], [HOA_ARC].[HOA Email],[HOA_ARC].[Contact Person], [HOA_ARC].[Date Approved] FROM [dbo].[Order] Inner Join [HOA_ARC] ON [dbo].[Order].HOAARC_ID = [HOA_ARC].HOAARC_ID ORDER BY [Date Approved]")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))



    def loadOrderCustomerInfo(self):
        result = self.cursor.execute("SELECT [dbo].[Order].Order_ID, Customer.Customer_ID, Customer.CustomerLastName, Customer.CustomerFirstName, Customer.CustomerEmail, Customer.CustomerPhone FROM [dbo].[Order] Inner Join Customer ON [dbo].[Order].Customer_ID = Customer.Customer_ID")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))
        
    
    def loadOrderPaymentMethod(self):
        result = self.cursor.execute("SELECT [dbo].[Order].Order_ID, Payment.Payment_ID, Payment.MethodOfPayment FROM [dbo].[Order] Left Join Payment ON [dbo].[Order].Payment_ID = Payment.Payment_ID")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))



    def loadPaidOrder(self):
        result = self.cursor.execute("SELECT [dbo].[Order].Order_ID, Payment.Payment_ID, Payment.AmountRemaining FROM [dbo].[Order] Left Join Payment ON [dbo].[Order].Payment_ID = Payment.Payment_ID WHERE AmountRemaining = 0")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))

    

    def loadCompletedProduction(self):
        result = self.cursor.execute("SELECT [dbo].[Order].Order_ID, Production.Production_ID, Production.CompletionDate FROM [dbo].[Order] INNER JOIN Production ON [dbo].[Order].Production_ID = Production.Production_ID WHERE CompletionDate IS NOT NULL")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))



    def loadMaterialSupplier(self):
        result = self.cursor.execute("SELECT Material.Material_ID,Material.MaterialName, Material.MaterialCost, Supplier.Supplier_ID FROM Material INNER JOIN Supplier ON Material.Supplier_ID = Supplier.Supplier_ID")
        self.ui.JOINTable.setRowCount(0)
        for row , row_data in enumerate(result):
            self.ui.JOINTable.insertRow(row)
            for column, column_data in enumerate(row_data):
                self.ui.JOINTable.setItem(row,column,QtWidgets.QTableWidgetItem(str(column_data)))





    #CONNECT TO SERVER FUNCTION
    def connection(self):
        try:
            server = self.ui.ServerLineEdit.text()
            database = self.ui.DatabaseLineEdit.text()
            uid = self.ui.UIDLineEdit.text()
            pwd = self.ui.PWDLineEdit.text()
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                        SERVER='+server+'; \
                        DATABASE='+database+'; \
                        UID='+uid+'; \
                        PWD='+ pwd)
            self.cursor = conn.cursor()
            self.ui.ConnectionPageMesssage.setText("SUCCESS!")
            return conn,self.cursor
            
        except:
            self.ui.ConnectionPageMesssage.setText("ERROR OCCURED CHECK INPUT OR CONNECTION AGAIN")




    #MODIFYING DATA FUNCTIONS

    def addData(self):
        try:
            tableName = self.ui.TableNameLineEdit.text()
            Values = self.ui.ValuesLineEdit.text()

            self.cursor.execute(("INSERT INTO %s VALUES %s")%(tableName,Values))
            self.ui.AddPageMessage.setText("SUCCESS!")
            self.cursor.commit()
        except:
            self.ui.AddPageMessage.setText("ERROR OCCURED CHECK INPUT AGAIN")

    def updateData(self):
        try:
            tableName =self.ui.TableNameLineEditUpdate.text()
            setClause = self.ui.SetLineEdit.text()
            toWhat =self.ui.ToWhatLineEdit.text()
            where = self.ui.WhereLineEdit.text()

            self.cursor.execute("UPDATE %s SET %s = '%s' WHERE %s;"%(tableName,setClause,toWhat,where))
            
            self.ui.UpdateMessageLabel.setText("SUCCESS")
            self.cursor.commit()
        except:
            self.ui.UpdateMessageLabel.setText("ERROR OCCURED CHECK INPUT AGAIN")

    def deleteData(self):
        try:
            tableName = self.ui.DeleteFromLineEdit.text()
            where = self.ui.DeleteWhereLineEdit.text()

            self.cursor.execute("DELETE FROM %s WHERE %s;"%(tableName,where))

            self.ui.DeletePageMessage.setText("SUCCESS")
            self.cursor.commit()
        except:
            self.ui.DeletePageMessage.setText("ERROR OCCURED CHECK INPUT AGAIN")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

        

