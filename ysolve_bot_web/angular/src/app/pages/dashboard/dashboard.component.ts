import { Component, ElementRef, OnInit } from '@angular/core';
//@ts-ignore
import anime from 'animejs';
import { RosService } from 'src/app/shared/services/ros.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  navigation: Navigation = Navigation.MANUAL;
  Navigation: typeof Navigation = Navigation;
  ManualNavigation: typeof ManualNavigation = ManualNavigation;
  AutomaticNavigation: typeof AutomaticNavigation = AutomaticNavigation;
  robotMenu: boolean = false;
  cameraMenu: boolean = false;
 
  constructor(private ros: RosService) {};

  ngOnInit(): void {
    this.move([0,0], [0, -200])
  }

  changeNavigation() {
    if (this.navigation == Navigation.AUTOMATIC) {
      this.navigation = Navigation.MANUAL;
    } else {
      this.navigation = Navigation.AUTOMATIC;
    }
  }

  toggleRobotMenu(status: boolean) {
    this.cameraMenu = false;
    this.robotMenu = status;
  }

  toggleCameraMenu(status: boolean) {
    this.robotMenu = false;
    this.cameraMenu = status;
  }

  move(x: any, y: any) {
    anime({
      targets: '.rbs',
      translateX: [x[0], x[1]],
      translateY: [y[0], y[1]],
      opacity: .2,
      delay: 500,
      duration: 2000,
      easing: 'easeInOutExpo',
      loop: true
    });
  }

  moveRight() {
    this.ros.moveRight().subscribe(res => {console.log(res)})
  }
  moveLeft() {
    this.ros.moveLeft().subscribe(res => {console.log(res)})
  }
  moveForward() {
    this.ros.moveForward().subscribe(res => {console.log(res)})
  }
  moveBack() {
    this.ros.moveBack().subscribe(res => {console.log(res)})
  }
  stopMove() {
    this.ros.stopMove().subscribe(res => {console.log(res)})
  }


  moveToA() {
  }
  moveToB() {
  }
  moveToC() {
  }
  moveToD() {
  }
  moveToE() {
  }
  moveToF() {
  }
  moveToAll() {
  }


  subscribe(){

  }

  connect(){
    this.ros.connect().subscribe(res => {console.log(res)})
  }

  disconnect(){
    this.ros.disconnect().subscribe(res => {console.log(res)})
  }  
}

enum Navigation {
  MANUAL,
  AUTOMATIC
}

enum ManualNavigation {
  FORWARD = "Hacia delante",
  BACK = "Hacia atrás",
  LEFT = "Izquierda",
  RIGHT = "Derecha",
  STOP = "Parar"
}

enum AutomaticNavigation {
  POINT_A = "Punto A",
  POINT_B = "Punto B",
  POINT_C = "Punto C",
  POINT_D = "Punto D",
  POINT_E = "Punto E",
  POINT_F = "Punto F",
  MOVE_ALL = "Hacer circuito"
}