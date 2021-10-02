import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home-menu',
  templateUrl: './home-menu.component.html',
  styleUrls: ['./home-menu.component.scss']
})
export class HomeMenuComponent implements OnInit {

  constructor(private _auth: AuthService, private _router: Router) { }

  ngOnInit(): void {
    this._token = localStorage.getItem("authentication");
    this._user = this._auth.getUserId();
    console.log('user', this._user);
    this._userId = this._user['user_id'];
    this._userRole = this._user['role'];
  }

  _token: string|null = null;
  _user: any;
  _userId: number = 0;
  _userRole: number = 0;

  navigate(screen: string): void{
    this._router.navigateByUrl(screen);
  }
}
