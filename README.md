# Informe del Proyecto

## Estudiantes
- Samuel Matias Escobar Bejarano - 56825
- Ignacio Lizarazu Aramayo - 47046

## IMPORTANTE
Para asegurar el correcto funcionamiento del proyecto, se deben seguir estos pasos:
- MODIFICAR el archivo `/fastapi/predictor` en la línea 3 para introducir el PATH absoluto donde se clonó el repositorio.
- En una terminal, navegar hasta la carpeta `/web/react-gun-detector/` y ejecutar `npm install`, seguido de `npm run start`.
- En una terminal diferente, dirigirse a la carpeta `/fastapi/` y ejecutar `uvicorn app:app --reload`.

## Detalles de los Archivos

### 1. `app.py` (Aplicación FastAPI)
- **Funcionalidad Actualizada**: Actúa como el backend, manejando la lógica de negocio y la interacción con el modelo de IA para detección de armas y análisis de posturas.
- **Características Clave Actualizadas**:
  - Incorpora algoritmos avanzados para detección de armas y análisis de posturas humanas.
  - Mejoras en el procesamiento de imágenes y manejo de datos.
  - Integración optimizada con el módulo `predictor`, mejorando la precisión y eficiencia en las predicciones.

### 2. `App.js` (Frontend React)
- **Funcionalidad Actualizada**: Interfaz de usuario para interactuar con el modelo de IA.
- **Características Clave Actualizadas**:
  - Interfaz intuitiva para la carga de imágenes y visualización de resultados.
  - Mejoras en la gestión del estado y presentación de los resultados del modelo de IA.

### 3. `predictor.py`
- **Funcionalidad Actualizada**: Contiene lógica avanzada para la detección de armas y el análisis de posturas humanas, utilizando técnicas de aprendizaje profundo y visión computacional.
- **Requisitos Actualizados**:
  - Dependencias actualizadas para soportar algoritmos avanzados de IA y procesamiento de imágenes.

## Pasos para Ejecutar la Aplicación
1. **Configuración del Backend (FastAPI)**: 
   - Verificar la instalación de Python y las bibliotecas requeridas.
   - Configurar correctamente `predictor.py`, incluyendo la especificación del PATH del repositorio.
   - Ejecutar `app.py` para iniciar el servidor FastAPI.
2. **Configuración del Frontend (React)**: 
   - Asegurar la instalación de Node.js y las dependencias de React.
   - Ejecutar la aplicación React a través de `App.js`.
3. **Interacción**: 
   - Usar el frontend de React para cargar archivos.
   - El backend procesa estos archivos y retorna los resultados para visualización en el frontend.

**Nota**: Este informe se ha actualizado para reflejar las mejoras en el modelo de IA y la interfaz de usuario, garantizando una experiencia más fluida y eficiente.
