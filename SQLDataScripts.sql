CREATE TABLE [HOA_ARC] (
  [HOAARC_ID] INT,
  [HOAARC Name] VARCHAR(50),
  [HOAARC Address] VARCHAR(225),
  [HOA Phone] VARCHAR(20),
  [HOA Email] VARCHAR(50),
  [Contact Person] VARCHAR(50),
  [Date Submitted] DATE,
  [Date Approved] DATE,
  PRIMARY KEY ([HOAARC_ID])
);

CREATE TABLE [Customer] (
  [Customer_ID] INT,
  [CustomerLastName] VARCHAR(50),
  [CustomerFirstName] VARCHAR(50),
  [CompanyName] VARCHAR(50),
  [CustomerPhone] VARCHAR(20),
  [CustomerEmail] VARCHAR(50),
  PRIMARY KEY ([Customer_ID])
);

CREATE TABLE [Supplier] (
  [Supplier_ID] INT,
  [SupplierAddress] VARCHAR(50),
  [SupplierName] VARCHAR(50),
  [SupplierPhone] VARCHAR(20),
  PRIMARY KEY ([Supplier_ID])
);

CREATE TABLE [Material] (
  [Material_ID] INT,
  [Supplier_ID] INT,
  [MaterialName] VARCHAR(50),
  [MaterialCost] DECIMAL(8,2),
  [MaterialQuantity] INT,
  [MaterialType] VARCHAR(50),
  PRIMARY KEY ([Material_ID]),
  CONSTRAINT [FK_Material.Supplier_ID]
    FOREIGN KEY ([Supplier_ID])
      REFERENCES [Supplier]([Supplier_ID])
);

CREATE TABLE [Production] (
  [Production_ID] INT,
  [StartDate] DATE,
  [CompletionDate] DATE,
  PRIMARY KEY ([Production_ID])
);

CREATE TABLE [Material_Product] (
  [Production_ID] INT,
  [Material_ID] INT,
  PRIMARY KEY ([Production_ID]),
  CONSTRAINT [FK_Material_Product.Production_ID]
    FOREIGN KEY ([Production_ID])
      REFERENCES [Production]([Production_ID])
);

CREATE TABLE [Payment] (
  [Payment_ID] INT,
  [DespositDate] DATE,
  [AmountRemaining] DECIMAL(8,2),
  [MethodOfPayment] VARCHAR(20),
  PRIMARY KEY ([Payment_ID])
);

CREATE TABLE [Permit] (
  [Permit_ID] INT,
  [PermitExpDate] DATE,
  [Date Applied] DATE,
  [Date Received] DATE,
  PRIMARY KEY ([Permit_ID])
);

CREATE TABLE [State] (
  [State_ID] INT,
  [StateName] VARCHAR(50),
  PRIMARY KEY ([State_ID])
);

CREATE TABLE [Country] (
  [Country_ID] INT,
  [CountryName] VARCHAR(50),
  PRIMARY KEY ([Country_ID])
);

CREATE TABLE [Installation Address] (
  [InstallationAddress_ID] INT,
  [State_ID] INT,
  [Country_ID] INT,
  [AddressLine1] VARCHAR(225),
  [AddressLine2] VARCHAR(225),
  [ZipCode] VARCHAR(10),
  [City] VARCHAR(50),
  PRIMARY KEY ([InstallationAddress_ID]),
  CONSTRAINT [FK_Installation Address.State_ID]
    FOREIGN KEY ([State_ID])
      REFERENCES [State]([State_ID]),
  CONSTRAINT [FK_Installation Address.Country_ID]
    FOREIGN KEY ([Country_ID])
      REFERENCES [COuntry]([Country_ID])
);

CREATE TABLE [Employee] (
  [Employee_ID] INT,
  [LastName] VARCHAR(50),
  [FirstName] VARCHAR(50),
  [Address] VARCHAR(225),
  [Phone] VARCHAR(20),
  [EmployeeType] VARCHAR(50),
  PRIMARY KEY ([Employee_ID])
);
CREATE TABLE [Installation] (
  [Installation_ID] INT,
  [InstallationAddress_ID] INT,
  [ProjectedInstallationDate] DATE,
  [ActualInstallationDate] DATE,
  [Installed] BIT,
  PRIMARY KEY ([Installation_ID]),
  CONSTRAINT [FK_Installation.InstallationAddress_ID]
    FOREIGN KEY ([InstallationAddress_ID])
      REFERENCES [Installation Address]([InstallationAddress_ID])
);

CREATE TABLE [Designer] (
  [Employee_ID] INT,
  [LastName] VARCHAR(50),
  [FirstName] VARCHAR(50),
  [Address] VARCHAR(225),
  [Phone] VARCHAR(20),
  [AssignedToJob] BIT,
  PRIMARY KEY ([Employee_ID]),
  CONSTRAINT [FK_Designer.Employee_ID]
    FOREIGN KEY ([Employee_ID])
      REFERENCES [Employee]([Employee_ID])
);

CREATE TABLE [Vehicle] (
  [LicensePlate_ID] INT,
  [VehicleMake] VARCHAR(50),
  [VehicleModel] VARCHAR(50),
  [VehicleYear] VARCHAR(10),
  [VehicleColor] VARCHAR(10),
  PRIMARY KEY ([LicensePlate_ID])
);

CREATE TABLE [Order] (
  [Order_ID] INT,
  [Customer_ID] INT,
  [Production_ID] INT,
  [Payment_ID] INT,
  [Installation_ID] INT,
  [Permit_ID] INT,
  [Employee_ID] INT,
  [HOAARC_ID] INT,
  PRIMARY KEY ([Order_ID]),
  CONSTRAINT [FK_Order.HOAARC_ID]
    FOREIGN KEY ([HOAARC_ID])
      REFERENCES [HOA_ARC]([HOAARC_ID]),
  CONSTRAINT [FK_Order.Customer_ID]
    FOREIGN KEY ([Customer_ID])
      REFERENCES [Customer]([Customer_ID]),
  CONSTRAINT [FK_Order.Permit_ID]
    FOREIGN KEY ([Permit_ID])
      REFERENCES [Permit]([Permit_ID]),
  CONSTRAINT [FK_Order.Installation_ID]
    FOREIGN KEY ([Installation_ID])
      REFERENCES [Installation]([Installation_ID]),
  CONSTRAINT [FK_Order.Employee_ID]
    FOREIGN KEY ([Employee_ID])
      REFERENCES [Designer]([Employee_ID])
);

CREATE TABLE [Welder] (
  [Employee_ID] INT,
  [LastName] VARCHAR(50),
  [FirstName] VARCHAR(50),
  [Address] VARCHAR(225),
  [Phone] VARCHAR(20),
  [AssignedToJob] BIT,
  PRIMARY KEY ([Employee_ID]),
  CONSTRAINT [FK_Welder.Employee_ID]
    FOREIGN KEY ([Employee_ID])
      REFERENCES [Employee]([Employee_ID])
);

CREATE TABLE [Fabricator] (
  [Employee_ID] INT,
  [LastName] VARCHAR(50),
  [FirstName] VARCHAR(50),
  [Address] VARCHAR(225),
  [Phone] VARCHAR(20),
  [AssignedToJob] BIT,
  PRIMARY KEY ([Employee_ID]),
  CONSTRAINT [FK_Fabricator.Employee_ID]
    FOREIGN KEY ([Employee_ID])
      REFERENCES [Employee]([Employee_ID])
);

CREATE TABLE [Contractor] (
  [Employee_ID] INT,
  [LastName] VARCHAR(50),
  [FirstName] VARCHAR(50),
  [Address] VARCHAR(225),
  [Phone] VARCHAR(20),
  [AssignedToJob] BIT,
  PRIMARY KEY ([Employee_ID]),
  CONSTRAINT [FK_Contractor.Employee_ID]
    FOREIGN KEY ([Employee_ID])
      REFERENCES [Employee]([Employee_ID])
);

CREATE TABLE [Driver] (
  [Employee_ID] INT,
  [LicensePlate_ID] INT,
  [LastName] VARCHAR(50),
  [FirstName] VARCHAR(50),
  [Address] VARCHAR(225),
  [Phone] VARCHAR(20),
  [AssignedToJob] BIT,
  PRIMARY KEY ([Employee_ID]),
  CONSTRAINT [FK_Driver.LicensePlate_ID]
    FOREIGN KEY ([LicensePlate_ID])
      REFERENCES [Vehicle]([LicensePlate_ID]),
  CONSTRAINT [FK_Driver.Employee_ID]
    FOREIGN KEY ([Employee_ID])
      REFERENCES [Employee]([Employee_ID])
);



ALTER TABLE [dbo].[Order]
ADD CONSTRAINT FK_Production_ID FOREIGN KEY (Production_ID) 
	REFERENCES Production(Production_ID);

ALTER TABLE [dbo].[Order]
ADD CONSTRAINT FK_Payment_ID FOREIGN KEY (Payment_ID) 
	REFERENCES Payment(Payment_ID);








--BULK IMPORTS 

BULK INSERT [dbo].[HOA_ARC]
FROM 'C:\Users\naimu\Downloads\Project CSVs\HOAARC CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Customer]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Customer CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Supplier]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Supplier CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Material]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Material CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Production]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Production CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Material_Product]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Associative MP CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Payment]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Payment CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Permit]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Permit CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[State]
FROM 'C:\Users\naimu\Downloads\Project CSVs\State CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Country]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Country CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Installation Address]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Installation Address CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Employee]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Employee CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Installation]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Installation CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Designer]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Designer CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Vehicle]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Vehicle CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Order]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Order CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Welder]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Welder CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Contractor]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Contractor CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Fabricator]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Fabricator CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);

BULK INSERT [dbo].[Driver]
FROM 'C:\Users\naimu\Downloads\Project CSVs\Driver CSV.csv'
WITH (
	FORMAT = 'CSV',
	FIRSTROW = 2,
	FIELDTERMINATOR =',',
	ROWTERMINATOR = '\n'
);


-- JOIN FOR EMPLOYEES NOT AT WORK
SELECT Employee.Employee_ID, Fabricator.LastName,Fabricator.FirstName
FROM Employee
INNER JOIN Fabricator ON Employee.Employee_ID = Fabricator.Employee_ID
WHERE AssignedToJob = 0


SELECT Employee.Employee_ID, [dbo].[Welder].LastName,[dbo].[Welder].FirstName
FROM Employee
INNER JOIN [dbo].[Welder] ON Employee.Employee_ID = [dbo].[Welder].Employee_ID
WHERE AssignedToJob = 0


SELECT Employee.Employee_ID, Contractor.LastName,Contractor.FirstName
FROM Employee
INNER JOIN Contractor ON Employee.Employee_ID = Contractor.Employee_ID
WHERE AssignedToJob = 0


SELECT Employee.Employee_ID, Designer.LastName,Designer.FirstName
FROM Employee
INNER JOIN Designer ON Employee.Employee_ID = Designer.Employee_ID
WHERE AssignedToJob = 0

SELECT Employee.Employee_ID, Driver.LastName,Driver.FirstName
FROM Employee
INNER JOIN Driver ON Employee.Employee_ID = Driver.Employee_ID
WHERE AssignedToJob = 0




--JOIN FOR EMPLOYEES AT WORK 

SELECT Employee.Employee_ID, Fabricator.LastName,Fabricator.FirstName
FROM Employee
INNER JOIN Fabricator ON Employee.Employee_ID = Fabricator.Employee_ID
WHERE AssignedToJob = 1


SELECT Employee.Employee_ID, [dbo].[Welder].LastName,[dbo].[Welder].FirstName
FROM Employee
INNER JOIN [dbo].[Welder] ON Employee.Employee_ID = [dbo].[Welder].Employee_ID
WHERE AssignedToJob = 1


SELECT Employee.Employee_ID, Contractor.LastName,Contractor.FirstName
FROM Employee
INNER JOIN Contractor ON Employee.Employee_ID = Contractor.Employee_ID
WHERE AssignedToJob = 1


SELECT Employee.Employee_ID, Designer.LastName,Designer.FirstName
FROM Employee
INNER JOIN Designer ON Employee.Employee_ID = Designer.Employee_ID
WHERE AssignedToJob = 1

SELECT Employee.Employee_ID, Driver.LastName,Driver.FirstName
FROM Employee
INNER JOIN Driver ON Employee.Employee_ID = Driver.Employee_ID
WHERE AssignedToJob = 1




-- Join of installation and installation addresses
SELECT Installation.Installation_ID, [Installation Address].InstallationAddress_ID,[Installation Address].AddressLine1,[Installation Address].AddressLine2,[Installation Address].ZipCode,[Installation Address].City
FROM Installation
Right Join [Installation Address] ON Installation.InstallationAddress_ID = [Installation Address].InstallationAddress_ID



--Join of Orders and projected installation dates sorted by soonest
SELECT [dbo].[Order].Order_ID, Installation.Installation_ID, Installation.ProjectedInstallationDate
FROM [dbo].[Order]
Inner Join Installation ON [dbo].[Order].Installation_ID = Installation.Installation_ID
ORDER BY ProjectedInstallationDate



--Join of Orders that have been installed
SELECT [dbo].[Order].Order_ID, Installation.Installation_ID, Installation.ActualInstallationDate
FROM [dbo].[Order]
Inner Join Installation ON [dbo].[Order].Installation_ID = Installation.Installation_ID


--Join of Orders and Permit information sorted by date received 
SELECT [dbo].[Order].Order_ID,Permit.Permit_ID,Permit.PermitExpDate,Permit.[Date Received]
FROM [dbo].[Order]
Inner Join Permit ON [dbo].[Order].Permit_ID = Permit.Permit_ID
ORDER BY [Date Received]


--Join of all Orders and their HOA Information sorted by date approved 
SELECT [dbo].[Order].Order_ID,[HOA_ARC].HOAARC_ID, [HOA_ARC].[HOAARC Name], [HOA_ARC].[HOAARC Address], [HOA_ARC].[HOA Phone], [HOA_ARC].[HOA Email],[HOA_ARC].[Contact Person], [HOA_ARC].[Date Approved]
FROM [dbo].[Order]
Inner Join [HOA_ARC] ON [dbo].[Order].HOAARC_ID = [HOA_ARC].HOAARC_ID
ORDER BY [Date Approved]


--Join of all orders and their customer contact info 
SELECT [dbo].[Order].Order_ID, Customer.Customer_ID, Customer.CustomerLastName, Customer.CustomerFirstName, Customer.CustomerEmail, Customer.CustomerPhone
FROM [dbo].[Order]
Inner Join Customer ON [dbo].[Order].Customer_ID = Customer.Customer_ID


--Join of the payment methods with the orders
SELECT [dbo].[Order].Order_ID, Payment.Payment_ID, Payment.MethodOfPayment
FROM [dbo].[Order]
Left Join Payment ON [dbo].[Order].Payment_ID = Payment.Payment_ID


--Join of Orders that have a Amount remaining of 0
SELECT [dbo].[Order].Order_ID, Payment.Payment_ID, Payment.AmountRemaining
FROM [dbo].[Order]
Left Join Payment ON [dbo].[Order].Payment_ID = Payment.Payment_ID
WHERE AmountRemaining = 0


--Join of Orders with completed Production (not null)
SELECT [dbo].[Order].Order_ID, Production.Production_ID, Production.CompletionDate
FROM [dbo].[Order]
INNER JOIN Production ON [dbo].[Order].Production_ID = Production.Production_ID
WHERE CompletionDate IS NOT NULL


--Join of all materials and its cost to suppliers
SELECT Material.Material_ID,Material.MaterialName, Material.MaterialCost, Supplier.Supplier_ID
FROM Material
INNER JOIN Supplier ON Material.Supplier_ID = Supplier.Supplier_ID