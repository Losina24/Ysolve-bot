import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-feature',
  templateUrl: './feature.component.html',
  styleUrls: ['./feature.component.scss']
})
export class FeatureComponent implements OnInit {

  @Input() title: string = "";
  @Input() text: string = "";
  @Input() icon: string = "";

  constructor() { }

  ngOnInit(): void {
  }

}
