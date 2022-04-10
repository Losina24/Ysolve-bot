import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard-element',
  templateUrl: './dashboard-element.component.html',
  styleUrls: ['./dashboard-element.component.scss']
})
export class DashboardElementComponent implements OnInit {

  @Input() property: string = "Propiedad";
  @Input() value: number | string = "---";

  constructor() { }

  ngOnInit(): void {
  }

}
