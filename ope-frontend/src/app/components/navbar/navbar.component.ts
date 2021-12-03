import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';
import { Component, HostListener, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  constructor(private router: Router, private _auth: AuthService) { }

  ngOnInit(): void {
    this.innerWidth = window.innerWidth;
    this.admin = this._auth.getUserId()['role'] === 1
  }

  signOut(){
    this._auth.signOut().subscribe(
      () => {
        window.location.reload();
      }
    );
  }

  admin = false;
  containerShows: boolean = false;
  innerWidth: any;

  @Input()
  appComponent: any;

  @HostListener('window:resize', ['$event'])
  onResize(event: any) {
    this.innerWidth = window.innerWidth;
  }

  navigate(screen: string): void{
    this.router.navigateByUrl(screen);
  }
}
