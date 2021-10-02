import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sub-menu-screen',
  templateUrl: './sub-menu-screen.component.html',
  styleUrls: ['./sub-menu-screen.component.scss']
})
export class SubMenuScreenComponent implements OnInit {

  constructor(private _router: Router) { }

  ngOnInit(): void {
  }

  navigate(to: string) : void {
    this._router.navigateByUrl(to);
  }

}
