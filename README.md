# **MultiBot by Ysolve (YsolveBot)**
Este repositorio contiene el software utilizado para el funcionamiento del YsolveBot, un robot terrestre modular pensado para ser facilmente integrable con distintos algoritmos de IA para su uso en diversos escenarios tales como: detección de incendios, análisis de cultivos, detección de gases peligrosos, grabación a distancia, reconocimiento del terreno, etc. Además, este repositorio también contiene aplicación web utilizada para poder controlar el YsolveBot de forma remota.

A continuación se describirán funcionalidades de ambas partes del proyecto, así como un manual de uso.

# **Contenido**
- [**Proyecto**](#multibot-by-ysolve-(ysolvebot))
- [**Contenidos**](#contenidos)
- [**ROS2**](#ros2)
    - [**Requisitos previos**](#requisitos-previos)
    - [**Empezando**](#empezando)
    - [**Estructura del proyecto**](#estructura-del-proyecto)
    - [**Paquetes**](#paquetes)
- [**Web**](#web)
    - [**Requerimientos previos**](#requerimientos-previos)
    - [**Comenzando**](#comenzando)
    - [**Estructura de la aplicación**](#estructura-de-la-aplicación)
    - [**Funcionalidades**](#funcionalidades)

# **ROS2**
Para desarrollar el YsolveBot utilizamos ***ROS2*** como framework o conjunto de herramientas para implementar distintas funcionalidades tales como la ***navegación manual***, la ***navegación autónoma***, la ***conexión entre el robot y la web***, el ***envío de ordenes***, etc. 