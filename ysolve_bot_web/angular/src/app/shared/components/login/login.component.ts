import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
  
  email: string = '';
  password: string = '';

  constructor(
    private _router: Router,
    private _route: ActivatedRoute
    ) {}

  ngOnInit(): void {}

  submit() {
    if (this.checkForm()) {
      this._router.navigate(['dash'], {relativeTo: this._route})
    }
  }

  checkForm() {
    console.log((this.email.length > 0 && this.password.length > 0))
    return (this.email.length > 0 && this.password.length > 0);
  }
}
