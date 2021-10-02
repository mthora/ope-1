import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home-screen',
  templateUrl: './home-screen.component.html',
  styleUrls: ['./home-screen.component.scss']
})
export class HomeScreenComponent implements OnInit {

  constructor() { }
  splashShows: boolean = true;
  ngOnInit(): void {
    setTimeout(()=>{
      this.splashShows = false;
    }, 1000)
  }
}
