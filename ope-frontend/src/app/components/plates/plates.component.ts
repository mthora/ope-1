import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-plates',
  templateUrl: './plates.component.html',
  styleUrls: ['./plates.component.scss']
})
export class PlatesComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  @Input() plateImage: string = '';
  @Input() plateName: string = '';
  @Input() plateDescription: string = '';
  @Input() platePrice: string = '';
  @Input() maxAmount: number = 10;

  plateAmount:number = 1;

  addAmount($event:any) : void {
    $event.stopPropagation();
    this.plateAmount < this.maxAmount ? this.plateAmount+=1 : this.plateAmount = this.maxAmount;
  }

  removeAmount($event:any) : void {
    $event.stopPropagation();
    this.plateAmount > 1 ? this.plateAmount-=1 : this.plateAmount = 1;
  }
}
