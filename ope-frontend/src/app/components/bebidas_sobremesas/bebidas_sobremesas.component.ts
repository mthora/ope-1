import { CartService } from './../../services/cart.service';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-bebidas_sobremesas',
  templateUrl: './bebidas_sobremesas.component.html',
  styleUrls: ['./bebidas_sobremesas.component.scss']
})
export class PlatesComponent implements OnInit {

  constructor(private _cart: CartService) { }

  ngOnInit() {
  }

  @Input() bebida_sobremesaImage: string = '';
  @Input() bebida_sobremesaName: string = '';
  @Input() bebida_sobremesaDescription: string = '';
  @Input() bebida_sobremesaPrice: string = '';
  @Input() maxAmount: number = 10;
  @Input() productId: number = 0;

  bebida_sobremesaAmount:number = 1;
  chosenProducts: any;

  addAmount($event:any) : void {
    $event.stopPropagation();
    this.bebida_sobremesaAmount < this.maxAmount ? this.bebida_sobremesaAmount+=1 : this.bebida_sobremesaAmount = this.maxAmount;
  }

  removeAmount($event:any) : void {
    $event.stopPropagation();
    this.bebida_sobremesaAmount > 1 ? this.bebida_sobremesaAmount-=1 : this.bebida_sobremesaAmount = 1;
  }

  updateCart(){
    this.chosenProducts = {
      "product_id": this.productId,
      "amount": this.bebida_sobremesaAmount
    }

    this._cart.addToCart(this.chosenProducts)
            .subscribe(
                (response) => {

                },
                () => {
                    console.log("deu ruim");
                }
            );
  }

}
