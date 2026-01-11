# 📦 Sistema de Gestión de Inventario (Backend)

Este proyecto es una aplicación de escritorio/web diseñada para que pequeñas empresas puedan llevar el control de sus productos, stock y categorías de manera eficiente.

### 🚀 ¿Por qué es especial este proyecto?
Este software comenzó usando consultas SQL manuales, pero fue evolucionado a un sistema moderno utilizando un **ORM (SQLAlchemy)** para mejorar la seguridad y permitir que funcione con cualquier base de datos (MySQL, PostgreSQL, etc.).

---

### 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.10+
* **Framework:** Flask (Para la API/Interfaz)
* **Base de Datos:** MySQL & SQLite
* **Manejador de BD:** SQLAlchemy (ORM)
* **Control de versiones:** Git & GitHub

---

### 🔧 Cómo instalarlo en tu PC

1. **Clona este repositorio:**
   git clone https://github.com/ricardosanchez24/proyecto-gestor-de-inventario

2. **Entra a la carpeta:**
   cd proyecto inventario

3. **Instala las dependencias necesarias:**
   pip install flask sqlalchemy mysql-connector-python

---

### 💻 Cómo usarlo

Para iniciar el programa, simplemente ejecuta el archivo principal:
python app.py

*El sistema creará automáticamente la base de datos si no existe gracias a la configuración de SQLAlchemy.*

---

### 🧠 Arquitectura y Lógica
- **Modelo de Datos:** Utilicé Programación Orientada a Objetos (POO) para definir los productos.
- **Migración Crítica:** Se eliminó el uso de `sqlite3.connect` para implementar `db.session` de SQLAlchemy, logrando un código más limpio y profesional.
- **Diseño y Arquitectura:** Se uso para el diseño de la arquitectura una hexagonal para desacoplar la logica, base de datos, las rutas de la API, etc. Con el fin de crear una app matenible y escalable, dividiendo el proyecto en capas como la capa de aplicación,infraestructura y domain. todo esto para una app robusta y segura que sigue buenas practicas

---

### 👤 Autor
* **Ricardo Sanchez** - *Estudiante de Ingeniería de Sistemas*
* LinkedIn: https://www.linkedin.com/in/ricardo-sanchez-b41850365/
