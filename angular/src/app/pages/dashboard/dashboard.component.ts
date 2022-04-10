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
  currentPoint: AutomaticNavigation | null = null;
 
  constructor(private ros: RosService) {};

  ngOnInit(): void {
    let o = Coords.getO();
    let m = Coords.getD();
    this.move(o[0], m[0], o[1], m[1])
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

  move(fromX: any, toX: any, fromY: any, toY: any) {
    anime({
      targets: '.rbs',
      top: [fromY, toY],
      left: [fromX, toX],
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
    this.ros.moveToA().subscribe(res => {
      let o = Coords.getO();
      let m = Coords.getA();
      this.move(o[0], m[0], o[1], m[1])
    })
  }
  moveToB() {
    this.ros.moveToB().subscribe(res => {
      let o = Coords.getO();
      let m = Coords.getB();
      this.move(o[0], m[0], o[1], m[1])
    })
  }
  moveToC() {
    this.ros.moveToC().subscribe(res => {
      let o = Coords.getO();
      let m = Coords.getC();
      this.move(o[0], m[0], o[1], m[1])
    })
  }
  moveToD() {
    this.ros.moveToD().subscribe(res => {
      let o = Coords.getO();
      let m = Coords.getD();
      this.move(o[0], m[0], o[1], m[1])
    })
  }
  moveToE() {
    this.ros.moveToE().subscribe(res => {
      let o = Coords.getO();
      let m = Coords.getE();
      this.move(o[0], m[0], o[1], m[1])
    })
  }
  moveToF() {
    this.ros.moveToF().subscribe(res => {
      let o = Coords.getO();
      let m = Coords.getF();
      this.move(o[0], m[0], o[1], m[1])
    })
  }
  moveToAll() {
    this.ros.moveToAll().subscribe(res => {console.log(res)})
  }


  subscribe(){
    this.ros.subs().subscribe(res => {console.log(res)})
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

class Coords {
  static getO() {
    return ['50%', '50%']
  }

  static getA() {
    return ['50%', '7%']
  } 

  static getB() {
    return ['10%', '20%']
  } 

  static getC() {
    return ['92%', '50%']
  }
  
  static getD() {
    return ['8%', '70%']
  }

  static getE() {
    return ['15%', '30%']
  }

  static getF() {
    return ['92%', '92%']
  }
}