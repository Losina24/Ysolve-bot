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
- [**Licencia**](#licencia)

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
Esta aplicación web ha sido desarrollada utilizando **Angular 12**, un framework que permite la creación de [Single-Page applications](https://es.wikipedia.org/wiki/Single-page_application) y la división de los elementos del frontend en componentes reutilizables. Además, se ha utilizado la libreri **Anime.js** para animar elementos de la interfaz gráfica y **Three.js** para implementar un motor gráfico que nos permita mostrar renders del robot en la web. Angular utiliza *TypeScript* y *Node.js*, por tanto, para poder ejecutar el servicio se deben instalar los siguientes paquetes:

- [Node.js](https://nodejs.org/en/download/)
- Angular:
```js
npm install -g @angular/cli
```

## **Comenzando**
1. Clonar el repositorio

```bash
git clone https://github.com/Losina24/Ysolve-bot
```

2. Instalar los paquetes

```bash
cd <path-to-directory>/Ysolve-bot/angular
npm install
```

3. Run Angular

```bash
ng serve --open
```

> Si el puerto 4200 ya está en uso
```bash
ng serve --port {port} --open
```

> Si quieres ejecutar el servicio sin abrir el navegador
```bash
ng serve
```

## **Estructura de la aplicación**
```
angular/
    ├── node_modules/
    └── src/
        ├── app/
        │   ├── pages/
        │   │   ├── dashboard
        │   │   └── landing-page
        │   ├── shared/
        │   │   ├── components/
        │   │   │   ├── layout/
        │   │   │   │   ├── alt-section
        │   │   │   │   ├── basic-section
        │   │   │   │   ├── feature
        │   │   │   │   ├── features-section
        │   │   │   │   ├── footer
        │   │   │   │   ├── header
        │   │   │   │   ├── main-cover
        │   │   │   │   ├── main-quote
        │   │   │   │   └── smartphone-render
        │   │   │   ├── login
        │   │   │   └── dashboard-element
        │   │   └── services/
        │   ├── app-routing.module.ts
        │   ├── app.component.html
        │   ├── app.component.scss
        │   ├── app.component.ts
        │   └── app.module.ts
        ├── assets/
        ├── enviroments/
        ├── favicon.ico
        ├── index.html
        ├── main.ts
        ├── polyfills.ts
        ├── styles.scss
        └── test.ts
```

## **Funcionalidades**

### Landing Page
La landing page es primera página que ve el usuario cuando entra. Su objetivo es mostrar las funcionalidades del producto al posible cliente. Hemos dividido esta página en distintas secciones, cada una en un componente distinto:

- **Header:** El es elemento que se muestra en la parte superior de la pantalla. Muestra el logotipo, un enlace a la página de Ysolve y un boton que abre el menú de login.
- **Main cover:** Este componente contiene la primera sección de la landing page, que muestra un título, con una imagen del robot y un call to action.
- **Main quote:** Contiene una cita que se muestra después del main cover. Sirve para separar secciones y enfatizar la calidad del producto.
- **Features section:** Esta sección contiene una imagen de la futura aplicación y una descripción de las funcionalidades del producto.
- **Basic section:** Esta sección contiene un texto básico y una imagen para acompañarlo.
- **Alt section:** Esta sección contiene un call to action que lleva a la página de Ysolve.
- **Footer:** El pie de página de la web.

### Login
Es un sencillo formulario con dos campos que permite al usuario acceder al dashboard del robot.

### Dashboard
El dashboard es la otra página implementada. Se utiliza como interfaz gráfica para comunicarse con el robot. Contiene las siguientes funcionalidades:

- **Menú de información:** Muestra una serie de etiquetas con información del robot como el nombre, la velocidad, el ángulo de giro, etc.
- **Mapa:** Es una representación visual del mundo por el cuál se mueve el robot. Tiene una serie de waypoints a los que el robot puede desplazarse desde el menú de navegación.
- **Menú de navegación:** Tiene dos modos: manual y automática. En el modo manual, se pueden enviar acciones al robot indicando la dirección en la que se debe mover. En modo automático, se le indica el punto al que quiere que se desplace.
- **Ver robot:** Es un menú activable que muestra un render del robot utilizando Three.js.
- **Ver cámara:** Es un menú activable que muestra vídeo en directo desde la cámara del robot (no implementado en el robot todavía).

 # **Licencia**
El código de este repositorio es propiedad de Ysolve.
Copyright © 2022, Ysolve.