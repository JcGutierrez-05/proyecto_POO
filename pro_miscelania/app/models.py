# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    cate_id = models.AutoField(db_column='Cate_Id', primary_key=True)  # Field name made lowercase.
    cate_nom = models.CharField(db_column='Cate_Nom', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'


class Ciudad(models.Model):
    ciud_id = models.AutoField(db_column='Ciud_Id', primary_key=True)  # Field name made lowercase.
    ciud_nom = models.CharField(db_column='Ciud_Nom', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    cliente_id = models.AutoField(db_column='Cliente_Id', primary_key=True)  # Field name made lowercase.
    cliente_nom = models.CharField(db_column='Cliente_Nom', max_length=60)  # Field name made lowercase.
    cliente_mail = models.CharField(db_column='Cliente_Mail', max_length=60)  # Field name made lowercase.
    cliente_tel = models.CharField(db_column='Cliente_Tel', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cliente_direc = models.CharField(db_column='Cliente_Direc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ciud = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='Ciud_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Compra(models.Model):
    compra_id = models.AutoField(db_column='Compra_Id', primary_key=True)  # Field name made lowercase.
    compra_fecha = models.DateField(db_column='Compra_fecha', blank=True, null=True)  # Field name made lowercase.
    prove = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='Prove_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compra'


class Envios(models.Model):
    envi_id = models.AutoField(db_column='Envi_Id', primary_key=True)  # Field name made lowercase.
    envi_fecha = models.DateField(db_column='Envi_Fecha', blank=True, null=True)  # Field name made lowercase.
    factura = models.ForeignKey('FacturaVenta', models.DO_NOTHING, db_column='Factura_Id', blank=True, null=True)  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_Id', blank=True, null=True)  # Field name made lowercase.
    ciud = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='Ciud_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'envios'


class FacturaCompraProducto(models.Model):
    factura = models.ForeignKey('FacturaVenta', models.DO_NOTHING, db_column='Factura_Id', blank=True, null=True)  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_Id', blank=True, null=True)  # Field name made lowercase.
    cantidad_producto = models.IntegerField(db_column='Cantidad_Producto', blank=True, null=True)  # Field name made lowercase.
    valor_compra = models.IntegerField(db_column='Valor_Compra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factura_compra_producto'


class FacturaProducto(models.Model):
    factura = models.ForeignKey('FacturaVenta', models.DO_NOTHING, db_column='Factura_Id', blank=True, null=True)  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_Id', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factura_producto'


class FacturaVenta(models.Model):
    factura_id = models.AutoField(db_column='Factura_Id', primary_key=True)  # Field name made lowercase.
    factura_fecha = models.DateField(db_column='Factura_Fecha', blank=True, null=True)  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factura_venta'


class Producto(models.Model):
    producto_id = models.AutoField(db_column='Producto_Id', primary_key=True)  # Field name made lowercase.
    producto_nom = models.CharField(db_column='Producto_Nom', max_length=50)  # Field name made lowercase.
    producto_precio = models.IntegerField(db_column='Producto_Precio')  # Field name made lowercase.
    cate = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='Cate_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoProvedor(models.Model):
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Producto_Id', blank=True, null=True)  # Field name made lowercase.
    prove = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='Prove_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto_provedor'


class Proveedor(models.Model):
    prove_id = models.AutoField(db_column='Prove_Id', primary_key=True)  # Field name made lowercase.
    prove_nom = models.CharField(db_column='Prove_Nom', max_length=60)  # Field name made lowercase.
    prove_mail = models.CharField(db_column='Prove_Mail', max_length=60)  # Field name made lowercase.
    prove_tel = models.CharField(db_column='Prove_Tel', max_length=60, blank=True, null=True)  # Field name made lowercase.
    prove_direc = models.CharField(db_column='Prove_Direc', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedor'
