import { Component, ElementRef, OnInit } from '@angular/core';
//@ts-ignore
import anime from 'animejs';
//@ts-ignore
import { RosService } from 'src/app/shared/services/ros.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
//@ts-ignore
export class DashboardComponent implements OnInit {

  navigation: Navigation = Navigation.MANUAL;
  Navigation: typeof Navigation = Navigation;
  ManualNavigation: typeof ManualNavigation = ManualNavigation;
  AutomaticNavigation: typeof AutomaticNavigation = AutomaticNavigation;
  robotMenu: boolean = false;
  cameraMenu: boolean = false;
  currentPoint: AutomaticNavigation | null = null;
  datos: any = {
    positionX: 0,
    positionY: 0,
    speed: 0
  }
  nav: string = "Manual";
  fire: number = 0.0;
  image: string = ""
  firePoint: string = "";
  modal: boolean = true;

  constructor(private ros: RosService) { };

  ngOnInit(): void {
    let o = Coords.getA();
    let m = Coords.getC();
    this.move(o[0], m[0], o[1], m[1])
  }

  changeNavigation() {
    if (this.navigation == Navigation.AUTOMATIC) {
      this.navigation = Navigation.MANUAL;
      this.nav = "Manual";
    } else {
      this.nav = "Automatic";
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

  closeModal() {
    this.modal = false;
  }

  moveRight() { this.ros.moveRight().subscribe(res => { console.log(res) }) }
  moveLeft() { this.ros.moveLeft().subscribe(res => { console.log(res) }) }
  moveForward() { this.ros.moveForward().subscribe(res => { console.log(res) }) }
  moveBack() { this.ros.moveBack().subscribe(res => { console.log(res) }) }
  stopMove() { this.ros.stopMove().subscribe(res => { console.log(res) }) }


  moveToA() { this.ros.moveToA().subscribe(res => { this.movement(Coords.getA()) }) }
  moveToB() { this.ros.moveToB().subscribe(res => { this.movement(Coords.getB()) }) }
  moveToC() { this.ros.moveToC().subscribe(res => { this.movement(Coords.getC()) }) }
  moveToD() { this.ros.moveToD().subscribe(res => { this.movement(Coords.getD()) }) }
  moveToE() { this.ros.moveToE().subscribe(res => { this.movement(Coords.getE()) }) }
  moveToF() { this.ros.moveToF().subscribe(res => { this.movement(Coords.getF()) }) }
  moveToAll() { this.ros.moveToAll().subscribe(res => { console.log(res) }) }

  getImage() {this.ros.getImage().subscribe(res => {
    this.fire = res.fireProbability
    this.image = res.lastImage
    setTimeout(() => {
      this.getImage();
    }, 5000)
  })}

  movement(m) {
    let o = this.fromCurrentPoint();
    this.move(o[0], m[0], o[1], m[1])
  }

  subscribe() {
    this.ros.subs().subscribe(res => {
      this.datos = res.result;
      console.log(res)
      setTimeout(() => {
        this.subscribe();
      }, 5000)
    })
  }

  connect() {
    this.ros.connect().subscribe(res => { console.log(res); this.subscribe(); this.getImage()})
  }

  disconnect() {
    this.ros.disconnect().subscribe(res => { console.log(res) })
  }

  fromCurrentPoint() {
    if (this.currentPoint == AutomaticNavigation.POINT_A) {
      return Coords.getA()
    } else if (this.currentPoint == AutomaticNavigation.POINT_B) {
      return Coords.getB()
    } else if (this.currentPoint == AutomaticNavigation.POINT_C) {
      return Coords.getC()
    } else if (this.currentPoint == AutomaticNavigation.POINT_D) {
      return Coords.getD()
    } else if (this.currentPoint == AutomaticNavigation.POINT_E) {
      return Coords.getE()
    } else {
      return Coords.getF()
    }
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