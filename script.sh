#!/bin/bash

# Crear estructura de carpetas
mkdir -p Ciencia-de-Datos-Productividad/{ejercicios,app_movil,modelos_ml,documentacion}

# Crear archivos base
echo "# Ciencia de Datos para Productividad" > Ciencia-de-Datos-Productividad/README.md
echo "Este repositorio contiene ejercicios de Ciencia de Datos y una app móvil en Flutter." >> Ciencia-de-Datos-Productividad/README.md

# Crear un archivo de requerimientos para Python
echo "pandas\nnumpy\nmatplotlib\nseaborn\nscikit-learn\nnltk\ntextblob\nflask" > Ciencia-de-Datos-Productividad/requirements.txt

# Crear archivos iniciales en cada carpeta
echo "# Carpeta de ejercicios de Ciencia de Datos" > Ciencia-de-Datos-Productividad/ejercicios/README.md
echo "# Carpeta para modelos de Machine Learning" > Ciencia-de-Datos-Productividad/modelos_ml/README.md
echo "# Carpeta para la documentación" > Ciencia-de-Datos-Productividad/documentacion/README.md

echo "// Proyecto Flutter con autenticación de Google" > Ciencia-de-Datos-Productividad/app_movil/README.md

# Inicializar Flutter
cd Ciencia-de-Datos-Productividad/app_movil
flutter create .
flutter pub add firebase_core firebase_auth google_sign_in

# Regresar al directorio raíz
cd ..

# Mensaje final
echo "Estructura inicial del proyecto creada exitosamente."
