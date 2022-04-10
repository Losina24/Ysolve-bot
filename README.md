# **MultiBot by Ysolve**
Este repositorio contiene el software utilizado para el funcionamiento del **MultiBot by Ysolve** (nos referiremos a él como YsolveBot en el resto de la documentación), un robot terrestre modular pensado para ser fácilmente integrable con distintos algoritmos de IA para su uso en diversos escenarios tales como: detección de incendios, análisis de cultivos, detección de gases peligrosos, grabación a distancia, reconocimiento del terreno, etc. Además, este repositorio también contiene aplicación web utilizada para poder controlar el YsolveBot de forma remota.

A continuación se describirán las funcionalidades de ambas partes del proyecto, así como un manual de uso.

# **Contenido**
- [**Proyecto**](#multibot-by-ysolve)
- [**Contenido**](#contenido)
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

## **Requisitos previos**
(Hay que describir las cosas que se tienen que instalar, ros2, paquetes, python, etc.)

## **Empezando**
(Hay que describir como arrancar el proyecto)

## **Estructura del proyecto**
(Hay que crear un árbol de directorios)

## **Paquetes**
(Hay que enumerar y explicar los paquetes que se han implementado)

# **Web**
La web cumple dos propósitos: dar a conocer el producto a nuevos clientes y servir como interfaz gráfica del robot. Con esto en mente, se ha divido en dos partes, la **landing page** y el **dashboard**.

## **Requerimientos previos**
Esta aplicación web ha sido desarrollada utilizando **Angular 12**, un framework que permite la creación de [Single-Page applications](https://es.wikipedia.org/wiki/Single-page_application) y la división de los elementos del frontend en componentes reutilizables. Este framework utiliza *TypeScript* y *Node.js*, por tanto, para poder ejecutar el servicio se deben instalar los siguientes paquetes:

- [Node.js](https://nodejs.org/en/download/)
- Angular:
```js
$ npm install -g @angular/cli
```

## **Comenzando**
1. Clonar el repositorio

```js
$ git clone https://github.com/Losina24/Ysolve-bot
```

2. Instalar los paquetes

```js
$ cd <path-to-directory>/Ysolve-bot/angular
$ npm install
```

3. Run Angular

```js
$ ng serve --open

// Si el puerto 4200 ya está en uso
$ ng serve --port {port} --open

// Si quieres ejecutar el servicio sin abrir el navegador
$ ng serve
```

## **Estructura de la aplicación**

