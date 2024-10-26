<p align="center">
    <a href="https://github.com/osiristape/ADC-Checker-tool/blob/main/README.md">English</a>  |   
    <a href="https://github.com/osiristape/ADC-Checker-tool/blob/main/manual_de_lectura.md">Español</a>  |  
    <a href="https://github.com/osiristape/ADC-Checker-tool/blob/main/自述文.md">Mandarin</a>
</p>

# Herramienta de Verificación ADC

Esta herramienta de Verificación ADC monitorea los endpoints del Controlador de Entrega de Aplicaciones (ADC), asegurando que sean accesibles, realizando verificaciones de latencia, validando certificados SSL/TLS y comprobando el estado de los servicios balanceados. Alerta al usuario por correo electrónico si se detectan problemas.

## Características

1. **Monitoreo de Disponibilidad**: Verifica si el endpoint del ADC es accesible.
2. **Verificación de Latencia**: Mide el tiempo de respuesta.
3. **Verificación de Endpoint de Salud**: Asegura que los servicios balanceados estén respondiendo.
4. **Validación SSL/TLS**: Verifica el estado del certificado SSL.
5. **Alertas**: Envía alertas si se detectan problemas.

## Requisitos Previos

- Python 3.8 o superior
- Pip para la gestión de paquetes
- Una conexión a internet activa

## Instalación

### Paso 1: Clonar el Repositorio
- En tu terminal o símbolo del sistema, navega al directorio deseado y ejecuta:

```bash
git clone https://github.com/osiristape/ADC-Checker-tool.git
cd ADC-Checker-tool
```

### Paso 2: Instalar Dependencias
- Instala los paquetes de Python necesarios con:

```bash
pip install -r requirements.txt
```

## Configuración
Edita config.py para agregar tus endpoints ADC y configurar las alertas:

- **ADC_ENDPOINTS**: Lista de endpoints ADC a monitorear.
- **ALERT_THRESHOLD**: Umbral de latencia en milisegundos.
- **ALERT_EMAIL**: Dirección de correo a la que se enviarán las alertas.
- **SMTP_SERVER**: Servidor SMTP para alertas por correo electrónico.
- **SMTP_PORT**: Puerto del servidor SMTP.
- **SMTP_USER** y **SMTP_PASSWORD**: Credenciales de inicio de sesión para el servidor SMTP.


Ejemplo de **config.py**:
```python
ADC_ENDPOINTS = [
    'https://example-adc1.com',
    'https://example-adc2.com'
]

ALERT_THRESHOLD = {
    'latency': 300
}

ALERT_EMAIL = "alert@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "user@example.com"
SMTP_PASSWORD = "password"
```

## Uso
### Ejecutar la Herramienta de Verificación ADC
1. Abre una terminal o símbolo del sistema en el directorio ADC-Checker-tool.
2. Ejecuta el siguiente comando:
   
   **En Windows:**
   ```powershell
   python adc_checker.py
   ```
   **En Linux:**
   ```bash
   python3 adc_checker.py
   ```

    La herramienta:
    - Realizará comprobaciones en cada endpoint.
    - Guardará los resultados en **logs/adc_checker.log.**
    - Enviará una alerta por correo si alguna comprobación falla.

---

### Programación (Opcional)
- Para automatizar las verificaciones, puedes programar el script para que se ejecute periódicamente:

**Windows**
1. Abre el Programador de Tareas.
2. Crea una nueva tarea.
3. Configura el campo "Programa/script" con:
   ```powershell
   python
   ```
4. Configura el campo "Agregar argumentos" con:
   ```powershell
   adc_checker.py
   ```
5. Configura el campo "Iniciar en" con el directorio donde se encuentra **adc_checker.py**.

**Linux**
- Para ejecutar el script a intervalos regulares (p.ej., cada hora), puedes usar cron:
1. Abre la tabla de cron:
```bash
   crontab -e
```
2. Agrega una entrada para ejecutar el script cada hora:
```bash
   0 * * * * /usr/bin/python3/path/to/ADC-Checker-tool/adc_checker.py
```
---

## Registro
- Los registros se guardan en **logs/adc_checker.log**. Revisa este archivo para obtener información detallada sobre cada verificación y errores.

## Solución de Problemas
- **No se envían alertas por correo**: Asegúrate de que los ajustes de SMTP sean correctos en config.py.
- **Errores de Certificado SSL/TLS**: Asegúrate de que los endpoints usen HTTPS.
- **Faltan Dependencias**: Ejecuta *pip install -r requirements.txt* para reinstalar las dependencias.

## Licencia
- Este proyecto está bajo la licencia MIT.

```yaml
Este README cubre la instalación, configuración, uso, programación y solución de problemas para entornos de Windows y Linux. ¡Déjame saber si deseas personalización adicional!
```

