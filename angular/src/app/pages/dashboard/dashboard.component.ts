import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  navigation: Navigation = Navigation.MANUAL;
  Navigation: typeof Navigation = Navigation;

  constructor() { }

  ngOnInit(): void {
  }

  changeNavigation() {
    if (this.navigation == Navigation.AUTOMATIC) {
      this.navigation = Navigation.MANUAL;
    } else {
      this.navigation = Navigation.AUTOMATIC;
    }
  }
}

enum Navigation {
  MANUAL,
  AUTOMATIC
}
