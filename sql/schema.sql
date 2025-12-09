
-- Auto-generated script based on RWVentas.csv
DROP TABLE IF EXISTS raw_sales;

CREATE TABLE raw_sales (
    Ciudad VARCHAR(255),
    Fecha VARCHAR(255),
    Producto VARCHAR(255),
    Tipo_Producto VARCHAR(255),
    Cantidad VARCHAR(255),
    Precio_Unitario VARCHAR(255),
    Tipo_Venta VARCHAR(255),
    Tipo_Cliente VARCHAR(255),
    Descuento VARCHAR(255),
    Costo_Envio VARCHAR(255),
    Total VARCHAR(255)
);
