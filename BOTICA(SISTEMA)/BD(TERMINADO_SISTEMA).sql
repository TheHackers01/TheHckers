
/****** Object:  Database [BD_LOGIN]    Script Date: 22/03/2023 20:58:46 ******/
CREATE DATABASE [BD_LOGIN4]
go
USE [BD_LOGIN4]
GO



/****** Object:  Table [dbo].[reportes]    Script Date: 22/03/2023 20:58:46 ******/

CREATE TABLE [dbo].[reportes](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[COD_PRODUCTOS] [nvarchar](50) NOT NULL,
	[NOMBRE] [varchar](1000) NULL,
	[STOCK] [int] NULL,
	[VALOR] [float] NULL,
	[ACCION] [VARCHAR](100) NULL)
go
/****** Object:  Table [dbo].[productos]    Script Date: 22/03/2023 20:58:46 ******/

CREATE TABLE [dbo].[productos](
	[COD_PRODUCTOS] [nvarchar](50) NOT NULL,
	[NOMBRE] [varchar](1000) NULL,
	[DESCRIPCION] [varchar](255) NULL,
	[STOCK] [int] NULL,
	[VALOR] [float] NULL,
	[FECHA_EXPEDICION] date,       ---nuevo
	[FECHA_COMPRA]  date, ---nuevo
	[FECHA_VENCIMIENTO] date, ---nuevo
	[MARCA] VARCHAR(30),
	Primary key(COD_PRODUCTOS))
go
CREATE TABLE [dbo].[registro_usuarios](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [varchar](50) NOT NULL,
	[apellido] [varchar](50) NOT NULL,
	[direccion] [varchar](100) NOT NULL,
	[rol] [varchar](50) NOT NULL,
	[numero] [int] NOT NULL,
	[usuario] [varchar](50) NOT NULL,
	[contrasena] [varchar](50) NOT NULL,
	Primary key(id))

GO
CREATE TABLE [dbo].[usuarios](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[usuario] [varchar](50) NOT NULL,
	[contrasena] [varchar](50) NOT NULL,
	Primary key(id))

GO																						 ---nuevo           ---nuevo             ---nuevo
INSERT [dbo].[productos] ([COD_PRODUCTOS], [NOMBRE], [DESCRIPCION],  [STOCK], [VALOR], [Fecha_expedicion],[FECHA_COMPRA], [Fecha_vencimiento], [Marca])
VALUES (N'BOT001', N'APRONAX', N'Medicamento antinflamatorio no esteroideo que se emplea en el tratamiento del dolor leve a moderado', 10, 20, '2022-01-01','2022-01-01','2027-12-31', 'Generico'),
       (N'BOT002', N'DULCOLAX', N'Laxante que aumenta la motilidad intestinal estimulando las terminaciones nerviosas de la pared intestinal.', 20, 40, '22-08-2022','22-06-2022','22-08-2027', 'Marca'),
       (N'BOT003', N'FURAZOLIDONA', N'Medicamento antinflamatorio no esteroideo que se emplea en el tratamiento del dolor leve a moderado', 18, 15, '28-07-2022','28-05-2022','28-07-2027', 'Generico'),
       (N'BOT004', N'MUCOTRIM', N'Broncodilatador mucolítico con acción expectorante y estimuladora del factor surfactante.', 9, 50, '21-06-2022','21-04-2022','21-06-2027', 'Marca'),
       (N'BOT005', N'BACTRIM', N'Medicamento antinflamatorio no esteroideo que se emplea en el tratamiento del dolor leve a moderado', 13, 12,'26-04-2022','26-02-2022','26-04-2027', 'Generico'),
       (N'BOT006', N'ERITROMICINA', N'La eritromicina pertenece a una clase de medicamentos llamados antibióticos macrólidos.', 11, 16,'16-05-2022','16-03-2022','16-05-2027', 'Marca'),
       (N'BOT007', N'HIOSCINA', N'Se utiliza para tratar el dolor y las molestias causadas por cólicos abdominales u otras actividades espasmódicas del aparato digestivo.', 15, 10, '25-04-2022','25-02-2022','25-04-2027', 'Marca'),
       (N'BOT008', N'OMEPRAZOL', N'El omeprazol de venta libre se usa para tratar la acidez estomacal frecuente ', 7, 25,'20-05-2022','20-03-2022','20-05-2027', 'Marca'),
       (N'BOT009', N'CLOTRIMAZOL', N'Usado para el tratamiento de infecciones tales como las infecciones vaginales por levaduras, candidiasis oral y dermatofitosis.', 12, 12, '16-06-2022','16-04-2022','16-06-2027', 'Generico'),
       (N'ALM001', N'GAMALATE', N'Tratamiento para trastornos cognitivos leve-moderados, que cursan con problemas de aprendizaje por dificultades de atención y memoria ', 21, 18, '12-05-2022','12-03-2022','12-05-2027', 'Marca'),
	   ------------------------
	    (N'ALM002', N'PARACETAMOL', N'Analgésico y antipirético de uso común para aliviar dolores de cabeza, fiebre y dolores musculares.', 30, 10, '2022-05-01','2022-03-01','2027-04-30', 'Generico'),
		(N'ALM003', N'IBUPROFENO', N'Medicamento antiinflamatorio no esteroideo que se emplea en el tratamiento del dolor leve a moderado.', 25, 15, '2022-06-15','2022-04-15','2027-06-14', 'Marca'),
		(N'ALM004', N'ACETAMINOFÉN', N'Analgésico y antipirético utilizado para tratar el dolor y la fiebre.', 20, 12, '2022-07-02','2022-05-02','2027-07-01', 'Generico'),
		(N'ALM005', N'ASPIRINA', N'Medicamento antiinflamatorio no esteroideo que se utiliza para tratar el dolor leve a moderado y la fiebre.', 15, 8, '2022-08-10','2022-06-10','2027-08-09', 'Marca'),
		(N'ALM006', N'RANITIDINA', N'Medicamento utilizado para tratar y prevenir las úlceras gástricas y la enfermedad por reflujo gastroesofágico.', 12, 20, '2022-09-25','2022-07-25','2027-09-24', 'Generico'),
		(N'ALM007', N'OMECLAMOX', N'Medicamento que combina omeprazol y claritromicina, utilizado para tratar las infecciones estomacales causadas por la bacteria Helicobacter pylori.', 8, 40, '2022-10-15','2022-08-15','2027-10-14', 'Marca'),
		(N'ALM008', N'KETOROLACO', N'Medicamento antiinflamatorio no esteroideo que se utiliza para aliviar el dolor moderado a severo.', 5, 30, '2022-11-07','2022-09-07','2027-11-06', 'Generico'),
		(N'ALM009', N'VITAMINA C', N'Suplemento vitamínico utilizado para prevenir y tratar los resfriados comunes.', 40, 5, '2022-12-30','2022-10-30','2027-12-29', 'Generico'),
		(N'INV001', N'VITAMINA D', N'Suplemento vitamínico utilizado para mantener la salud de los huesos y prevenir enfermedades como el raquitismo.', 35, 7, '2023-01-15','2022-11-15','2028-01-14', 'Marca')
GO
SET IDENTITY_INSERT [dbo].[registro_usuarios] ON 

INSERT [dbo].[registro_usuarios] ([id], [nombre], [apellido], [direccion], [rol], [numero], [usuario], [contrasena]) VALUES (16, N'Marco', N'Arias', N'Los Angeles', N'Almacen', 993032490 , N'marco', N'123456')
INSERT [dbo].[registro_usuarios] ([id], [nombre], [apellido], [direccion], [rol], [numero], [usuario], [contrasena]) VALUES (17, N'Henry', N'Villanueva', N'Lima', N'Almacen',411921556, N'henry', N'123456')
SET IDENTITY_INSERT [dbo].[registro_usuarios] OFF
GO
SET IDENTITY_INSERT [dbo].[usuarios] ON 

INSERT [dbo].[usuarios] ([id], [usuario], [contrasena]) VALUES (16, N'marco', N'123456')
INSERT [dbo].[usuarios] ([id], [usuario], [contrasena]) VALUES (17, N'henry', N'123456')
SET IDENTITY_INSERT [dbo].[usuarios] OFF
GO
/****** Object:  Trigger [dbo].[registro_usuarios_after_insert]    Script Date: 22/03/2023 20:58:46 ******/

CREATE TRIGGER [dbo].[registro_usuarios_after_insert]
ON [dbo].[registro_usuarios]
AFTER INSERT
AS
BEGIN
  INSERT INTO usuarios (usuario, contrasena)
  SELECT usuario, contrasena FROM inserted;
END;
GO
ALTER TABLE [dbo].[registro_usuarios] ENABLE TRIGGER [registro_usuarios_after_insert]
GO
ALTER DATABASE [BD_LOGIN] SET  READ_WRITE 
GO


CREATE TRIGGER dbo.reporte
ON dbo.productos
AFTER DELETE
AS
BEGIN
  INSERT INTO dbo.reportes (COD_PRODUCTOS, NOMBRE, STOCK, VALOR, ACCION)
  SELECT deleted.COD_PRODUCTOS, deleted.NOMBRE, deleted.STOCK, deleted.VALOR, 'Eliminado' + ' el ' + CONVERT(varchar, GETDATE(), 120)
  FROM deleted
END

go

create trigger dbo.reporte2
on  dbo.productos
AFTER UPDATE 
as
begin 
	insert into dbo.reportes (COD_PRODUCTOS,NOMBRE, STOCK , VALOR , ACCION)
		SELECT deleted.COD_PRODUCTOS,deleted.NOMBRE, deleted.STOCK, deleted.VALOR,'Actualizado'+ ' el ' + CONVERT(varchar, GETDATE(), 120)
		FROM deleted
end;
UPDATE dbo.productos
SET NOMBRE = 'ada'
WHERE COD_PRODUCTOS = 'BOT020';

CREATE TRIGGER dbo.reporte3
ON dbo.productos
AFTER INSERT
AS
BEGIN
  INSERT INTO dbo.reportes (COD_PRODUCTOS, NOMBRE, STOCK, VALOR, ACCION)
  SELECT inserted.COD_PRODUCTOS, inserted.NOMBRE, inserted.STOCK, inserted.VALOR, 'Agregado' + ' el ' + CONVERT(varchar, GETDATE(), 120)
  FROM inserted
END

