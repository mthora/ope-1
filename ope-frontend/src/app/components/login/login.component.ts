import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import {MatSnackBar} from '@angular/material/snack-bar';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(private _auth: AuthService, private _router: Router, private _snackBar: MatSnackBar) { }

  ngOnInit(): void {
    this.navigateIfLogged();
  }

  formErrors: string[] = [];

  credentials = new FormGroup(
    {
      email: new FormControl(''),
      password: new FormControl('')
    }
  );

  openSnackBar(messages: string[]){
    for (let message of messages){
      this._snackBar.open(message, "OK", {duration: 5000})
    }
  }

  navigateIfLogged(): void {
    var token = this._auth.accessToken;
    if (token != ''){
      this._router.navigateByUrl('');
    }
  }

  loginWithCredentials(): void {
    const credentialsJson = this.credentials.value
    this._auth.signIn(credentialsJson)
            .subscribe(
                (response) => {
                    localStorage.setItem("authentication", response.data)
                    this._router.navigateByUrl('')
                },
                (response) => {
                    this.formErrors = response.error.errors;
                    this.openSnackBar(this.formErrors);
                }
            );
  }
}
