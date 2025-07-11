import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog
import os
import json
import pandas as pd


try:
    from fpdf import FPDF
    HAS_FPDF = True
except ImportError:
    HAS_FPDF = False
    

# Cargar los datos desde un archivo JSON
def cargar_datos():
    if os.path.exists("datos.json"):
        with open("datos.json", "r") as archivo:
            return json.load(archivo)
    return []

# Guardar los datos en un archivo JSON
def guardar_datos():
    with open("datos.json", "w") as archivo:
        json.dump(ordenes_de_compra, archivo)

# Inicializar las órdenes de compra cargadas
ordenes_de_compra = cargar_datos()

def ingresar_orden():
    nombre = entry_op_nombre.get()
    fecha_emision = entry_op_fecha.get()
    monto = entry_op_monto.get()
    codigo = entry_op_codigo.get()
    
    if not (nombre and fecha_emision and monto and codigo):
        messagebox.showerror("Error", "Por favor, rellena todos los campos de la orden de compra.")
        return
    
    try:
        monto = float(monto)
    except ValueError:
        messagebox.showerror("Error", "El monto debe ser un número.")
        return
    
    for orden in ordenes_de_compra:
        if orden["codigo"] == codigo:
            messagebox.showerror("Error", "El código de orden ya existe.")
            return

    orden = {
        "nombre": nombre,
        "fecha_emision": fecha_emision,
        "monto_total": monto,
        "codigo": codigo,
        "facturas_asociadas": []
    }
    ordenes_de_compra.append(orden)
    messagebox.showinfo("Éxito", "Orden de compra ingresada correctamente.")
    entry_op_nombre.delete(0, tk.END)
    entry_op_fecha.delete(0, tk.END)
    entry_op_monto.delete(0, tk.END)
    entry_op_codigo.delete(0, tk.END)
    actualizar_combobox()
    actualizar_treeview()
    guardar_datos()  # Guardar después de agregar la orden

def ingresar_factura():
    numero = entry_fac_numero.get()
    fecha_emision = entry_fac_fecha.get()
    fecha_vencimiento = entry_fac_vencimiento.get()
    monto = entry_fac_monto.get()
    codigo_orden = combobox_op.get()
    
    if not (numero and fecha_emision and fecha_vencimiento and monto and codigo_orden):
        messagebox.showerror("Error", "Por favor, completa todos los campos de la factura.")
        return
    
    try:
        monto = float(monto)
    except ValueError:
        messagebox.showerror("Error", "El monto debe ser un número.")
        return

    orden_encontrada = next((orden for orden in ordenes_de_compra if orden["codigo"] == codigo_orden), None)
    if orden_encontrada is None:
        messagebox.showerror("Error", "Orden de compra no encontrada.")
        return

    factura = {
        "numero": numero,
        "fecha_emision": fecha_emision,
        "fecha_vencimiento": fecha_vencimiento,
        "monto": monto
    }
    orden_encontrada["facturas_asociadas"].append(factura)
    messagebox.showinfo("Éxito", "Factura agregada correctamente a la orden de compra.")
    entry_fac_numero.delete(0, tk.END)
    entry_fac_fecha.delete(0, tk.END)
    entry_fac_vencimiento.delete(0, tk.END)
    entry_fac_monto.delete(0, tk.END)
    actualizar_treeview()
    guardar_datos()  # Guardar después de agregar la factura

def actualizar_combobox():
    codigos = [orden["codigo"] for orden in ordenes_de_compra]
    combobox_op['values'] = codigos

def actualizar_treeview():
    for row in treeview.get_children():
        treeview.delete(row)
    for orden in ordenes_de_compra:
        monto_facturas = sum(f["monto"] for f in orden["facturas_asociadas"])
        monto_disponible = orden["monto_total"] - monto_facturas
        treeview.insert("", tk.END, iid=orden["codigo"],
                        values=(orden["codigo"], orden["nombre"], orden["fecha_emision"], orden["monto_total"], monto_disponible))

def on_treeview_select(event):
    selected = treeview.focus()
    if not selected:
        return
    orden = next((orden for orden in ordenes_de_compra if orden["codigo"] == selected), None)
    if orden:
        actualizar_treeview_facturas(orden)

def actualizar_treeview_facturas(orden):
    for row in treeview_fac.get_children():
        treeview_fac.delete(row)
    for factura in orden["facturas_asociadas"]:
        treeview_fac.insert("", tk.END, values=(factura["numero"], factura["fecha_emision"], factura["fecha_vencimiento"], factura["monto"]))

# Funciones de modificación y eliminación
def modificar_orden():
    selected = treeview.focus()
    if not selected:
        messagebox.showerror("Error", "Selecciona una orden para modificar.")
        return
    orden = next((orden for orden in ordenes_de_compra if orden["codigo"] == selected), None)
    if orden:
        entry_op_nombre.delete(0, tk.END)
        entry_op_nombre.insert(0, orden["nombre"])
        entry_op_fecha.delete(0, tk.END)
        entry_op_fecha.insert(0, orden["fecha_emision"])
        entry_op_monto.delete(0, tk.END)
        entry_op_monto.insert(0, orden["monto_total"])
        entry_op_codigo.delete(0, tk.END)
        entry_op_codigo.insert(0, orden["codigo"])
        btn_guardar_orden["command"] = lambda: guardar_modificacion_orden(orden)

def guardar_modificacion_orden(orden):
    nombre = entry_op_nombre.get()
    fecha_emision = entry_op_fecha.get()
    monto = entry_op_monto.get()
    codigo = entry_op_codigo.get()
    
    if not (nombre and fecha_emision and monto and codigo):
        messagebox.showerror("Error", "Por favor, rellena todos los campos de la orden de compra.")
        return
    
    try:
        monto = float(monto)
    except ValueError:
        messagebox.showerror("Error", "El monto debe ser un número.")
        return
    
    orden["nombre"] = nombre
    orden["fecha_emision"] = fecha_emision
    orden["monto_total"] = monto
    orden["codigo"] = codigo
    
    messagebox.showinfo("Éxito", "Orden de compra modificada correctamente.")
    actualizar_treeview()
    guardar_datos()  # Guardar después de modificar la orden

def eliminar_orden():
    selected = treeview.focus()
    if not selected:
        messagebox.showerror("Error", "Selecciona una orden para eliminar.")
        return
    respuesta = messagebox.askyesno("Eliminar Orden", "¿Estás seguro de que deseas eliminar esta orden?")
    if respuesta:
        orden = next((orden for orden in ordenes_de_compra if orden["codigo"] == selected), None)
        if orden:
            ordenes_de_compra.remove(orden)
            actualizar_treeview()
            guardar_datos()  # Guardar después de eliminar la orden
            messagebox.showinfo("Éxito", "Orden de compra eliminada correctamente.")

def modificar_factura():
    selected_orden = treeview.focus()
    if not selected_orden:
        messagebox.showerror("Error", "Selecciona una orden para modificar la factura.")
        return
    orden = next((orden for orden in ordenes_de_compra if orden["codigo"] == selected_orden), None)
    if orden:
        selected_factura = treeview_fac.focus()
        if not selected_factura:
            messagebox.showerror("Error", "Selecciona una factura para modificar.")
            return
        factura = orden["facturas_asociadas"][treeview_fac.index(selected_factura)]
        
        entry_fac_numero.delete(0, tk.END)
        entry_fac_numero.insert(0, factura["numero"])
        entry_fac_fecha.delete(0, tk.END)
        entry_fac_fecha.insert(0, factura["fecha_emision"])
        entry_fac_vencimiento.delete(0, tk.END)
        entry_fac_vencimiento.insert(0, factura["fecha_vencimiento"])
        entry_fac_monto.delete(0, tk.END)
        entry_fac_monto.insert(0, factura["monto"])
        btn_guardar_factura["command"] = lambda: guardar_modificacion_factura(factura, orden)

def guardar_modificacion_factura(factura, orden):
    factura["numero"] = entry_fac_numero.get()
    factura["fecha_emision"] = entry_fac_fecha.get()
    factura["fecha_vencimiento"] = entry_fac_vencimiento.get()
    try:
        factura["monto"] = float(entry_fac_monto.get())
    except ValueError:
        messagebox.showerror("Error", "El monto debe ser un número.")
        return

    messagebox.showinfo("Éxito", "Factura modificada correctamente.")
    actualizar_treeview_facturas(orden)
    guardar_datos()  # Guardar después de modificar la factura

def eliminar_factura():
    selected_orden = treeview.focus()
    if not selected_orden:
        messagebox.showerror("Error", "Selecciona una orden para eliminar la factura.")
        return
    orden = next((orden for orden in ordenes_de_compra if orden["codigo"] == selected_orden), None)
    if orden:
        selected_factura = treeview_fac.focus()
        if not selected_factura:
            messagebox.showerror("Error", "Selecciona una factura para eliminar.")
            return
        factura = orden["facturas_asociadas"][treeview_fac.index(selected_factura)]
        respuesta = messagebox.askyesno("Eliminar Factura", "¿Estás seguro de que deseas eliminar esta factura?")
        if respuesta:
            orden["facturas_asociadas"].remove(factura)
            actualizar_treeview_facturas(orden)
            guardar_datos()  # Guardar después de eliminar la factura
            messagebox.showinfo("Éxito", "Factura eliminada correctamente.")

# Interfaz gráfica
root = tk.Tk()
root.title("Sistema de Órdenes de Compra y Facturas")
root.geometry("900x700")
root.configure(bg="#f0f8ff")

style = ttk.Style(root) 
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))

notebook = ttk.Notebook(root) 
notebook.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
tab1 = ttk.Frame(notebook) 
notebook.add(tab1, text="Orden de Compra")

ttk.Label(tab1, text="Nombre de Orden:").grid(row=0, column=0, padx=5, pady=5, sticky="w") 
entry_op_nombre = ttk.Entry(tab1) 
entry_op_nombre.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(tab1, text="Fecha de Emisión:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_op_fecha = ttk.Entry(tab1) 
entry_op_fecha.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(tab1, text="Monto Total:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_op_monto = ttk.Entry(tab1) 
entry_op_monto.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(tab1, text="Código de Orden:").grid(row=3, column=0, padx=5, pady=5, sticky="w") 
entry_op_codigo = ttk.Entry(tab1) 
entry_op_codigo.grid(row=3, column=1, padx=5, pady=5)

btn_guardar_orden = ttk.Button(tab1, text="Ingresar Orden", command=ingresar_orden) 
btn_guardar_orden.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Factura")

ttk.Label(tab2, text="Número de Factura:").grid(row=0, column=0, padx=5, pady=5, sticky="w") 
entry_fac_numero = ttk.Entry(tab2) 
entry_fac_numero.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(tab2, text="Fecha de Emisión:").grid(row=1, column=0, padx=5, pady=5, sticky="w") 
entry_fac_fecha = ttk.Entry(tab2) 
entry_fac_fecha.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(tab2, text="Fecha de Vencimiento:").grid(row=2, column=0, padx=5, pady=5, sticky="w") 
entry_fac_vencimiento = ttk.Entry(tab2)
entry_fac_vencimiento.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(tab2, text="Monto de Factura:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_fac_monto = ttk.Entry(tab2) 
entry_fac_monto.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(tab2, text="Código de Orden:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
combobox_op = ttk.Combobox(tab2) 
combobox_op.grid(row=4, column=1, padx=5, pady=5)

btn_guardar_factura = ttk.Button(tab2, text="Ingresar Factura", command=ingresar_factura) 
btn_guardar_factura.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Órdenes y Facturas")
#tabla de ordenes
treeview = ttk.Treeview(tab3, columns=("Código", "Nombre", "Fecha", "Monto Total", "Monto Disponible")) 
treeview.heading("#0", text="ID") 
treeview.heading("Código", text="Código")
treeview.heading("Nombre", text="Nombre")
treeview.heading("Fecha", text="Fecha Emisión") 
treeview.heading("Monto Total", text="Monto Total") 
treeview.heading("Monto Disponible", text="Monto Disponible") 
treeview.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
#tabla de facturas
treeview_fac = ttk.Treeview(tab3, columns=("Número", "Fecha Emisión", "Fecha Vencimiento", "Monto")) 
treeview_fac.heading("#0", text="ID") 
treeview_fac.heading("Número", text="Número") 
treeview_fac.heading("Fecha Emisión", text="Fecha Emisión") 
treeview_fac.heading("Fecha Vencimiento", text="Fecha Vencimiento") 
treeview_fac.heading("Monto", text="Monto") 
treeview_fac.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
# Establecer color de fondo para la ventana principal
root.config(bg="#F0F8FF")  # Fondo azul claro

# Crear un estilo para los botones y frames
style = ttk.Style()

# Establecer colores para los botones
style.configure("TButton",
                background="#87CEFA",  # Color de fondo azul claro
                foreground="black",    # Color del texto en negro
                font=("Helvetica", 12))  # Fuente y tamaño de texto

# Establecer el estilo para el frame (sin bg, solo con estilo)
style.configure("TFrame",
                background="#F0F8FF")  # Fondo azul claro para el frame

# Crear un frame para los botones y colocarlo en el centro
frame_botones = ttk.Frame(tab3, style="TFrame")
frame_botones.grid(row=2, column=0, columnspan=3, pady=10)

# Configuración para centrar el frame
frame_botones.grid_columnconfigure(0, weight=1)  # Columna 0 con peso para centrar
frame_botones.grid_columnconfigure(1, weight=1)  # Columna 1 con peso para centrar
frame_botones.grid_columnconfigure(2, weight=1)  # Columna 2 con peso para centrar

# Botones de modificación y eliminación centrados dentro del frame con el estilo aplicado
btn_modificar_orden = ttk.Button(frame_botones, text="Modificar Orden", command=modificar_orden, style="TButton")
btn_modificar_orden.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

btn_eliminar_orden = ttk.Button(frame_botones, text="Eliminar Orden", command=eliminar_orden, style="TButton")
btn_eliminar_orden.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

btn_modificar_factura = ttk.Button(frame_botones, text="Modificar Factura", command=modificar_factura, style="TButton")
btn_modificar_factura.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

btn_eliminar_factura = ttk.Button(frame_botones, text="Eliminar Factura", command=eliminar_factura, style="TButton")
btn_eliminar_factura.grid(row=3, column=1, padx=5, pady=5, sticky="ew")


#carga de datos iniciales
actualizar_combobox() 
actualizar_treeview()

root.mainloop()