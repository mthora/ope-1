import { CartService } from './../../services/cart.service';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-plates',
  templateUrl: './plates.component.html',
  styleUrls: ['./plates.component.scss']
})
export class PlatesComponent implements OnInit {

  constructor(private _cart: CartService) { }

  ngOnInit() {
  }

  @Input() plateImage: string = '';
  @Input() plateName: string = '';
  @Input() plateDescription: string = '';
  @Input() platePrice: string = '';
  @Input() maxAmount: number = 10;
  @Input() productId: number = 0;

  plateAmount:number = 1;
  chosenProducts: any;

  addAmount($event:any) : void {
    $event.stopPropagation();
    this.plateAmount < this.maxAmount ? this.plateAmount+=1 : this.plateAmount = this.maxAmount;
  }

  removeAmount($event:any) : void {
    $event.stopPropagation();
    this.plateAmount > 1 ? this.plateAmount-=1 : this.plateAmount = 1;
  }

  updateCart(){
    this.chosenProducts = {
      "product_id": this.productId,
      "amount": this.plateAmount
    }

    this._cart.addToCart(this.chosenProducts)
            .subscribe(
                (response) => {
                    console.log(response);
                },
                () => {
                    console.log("deu ruim");
                }
            );
  }

}
