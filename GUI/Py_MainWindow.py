import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from matplotlib.pyplot import show

from Ui_MainWindow import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)



        #SET STARTING WIDGET TO Home_Page
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home_page)




        #WHAT CLICKING EACH BUTTON WILL DO (CALL FUNCTION BELOW)
        self.ui.Add_button.clicked.connect(self.showAdd)
        self.ui.Contractor_button.clicked.connect(self.showContractor)
        self.ui.Contractor_button.clicked.connect(self.showCountry)
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




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

        

