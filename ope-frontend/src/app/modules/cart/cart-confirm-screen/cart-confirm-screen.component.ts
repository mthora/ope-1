import { CartService } from './../../../services/cart.service';
import { Router } from '@angular/router';
import { Component, NgZone, OnInit, ViewChild } from '@angular/core';
import {CdkTextareaAutosize} from '@angular/cdk/text-field';
import { take } from 'rxjs/operators';
import { FormControl, FormGroup } from '@angular/forms';
import { forkJoin } from 'rxjs';

@Component({
  selector: 'app-cart-confirm-screen',
  templateUrl: './cart-confirm-screen.component.html',
  styleUrls: ['./cart-confirm-screen.component.scss']
})
export class CartConfirmScreenComponent implements OnInit {

  constructor(private router: Router, private cart: CartService, private _ngZone: NgZone) { }
  @ViewChild('autosize') autosize!: CdkTextareaAutosize;
  ngOnInit(): void {
    console.log(this.cart.order)
    this.hasProducts = this.cart.order.length != 0
    for (let i of this.cart.order) {
        this.sumList.push(parseFloat(i.price) * parseInt(i.amount));
      }
      this.orderSum = this.sumList.reduce((a, b) => a + b, 0);
      this.tip = this.orderSum*0.1;
    }

  order = new FormGroup({
    consumed_in: new FormControl(),
    table: new FormControl(0),
    payment_method: new FormControl(),
    obs: new FormControl("")
  })

  triggerResize() {
    // Wait for changes to be applied, then trigger textarea resize.
    this._ngZone.onStable.pipe(take(1))
        .subscribe(() => this.autosize.resizeToFitContent(true));
  }

  cartUpdated(e: any) {
    this.hasProducts = this.cart.order.length != 0;
    this.sumList = [];
    for (let i of this.cart.order) {
        this.sumList.push(parseFloat(i.price) * parseInt(i.amount));
    }
    this.orderSum = this.sumList.reduce((a, b) => a + b, 0);
    this.tip = this.orderSum*0.1;
  }

  reload = false;
  hasProducts: boolean = false;
  sumList: any[] = [];
  orderSum: number = 0;
  tip: number = 0;
  id = null;

  deliveryOptions = [{desc: "Entrega na mesa", id: 1}, {desc:"Retirar no local", id: 2}]

  navigate(screen: string): void{
    this.router.navigateByUrl(screen);
  }

  endOrder(){
    const order = this.order.value;
    this.cart.sendOrder(order)
    .subscribe(
      (response) => {
        this.id = response.id;
        let listOfObservables: any[] = []
            for (let i of this.cart.order) {
              listOfObservables.push(
                this.cart.addProductOrder({
                    "order_id": parseInt(response.id),
                    "product_id": parseInt(i.product_id),
                    "price": parseFloat(i.price).toFixed(2),
                    "amount": parseInt(i.amount)
                  })
              )
            }
        forkJoin(listOfObservables).subscribe(
          (res) => {
            console.log(res);
            let previousOrder = localStorage.getItem('order-id');
            if (previousOrder == null) {
              localStorage.setItem('order-id', JSON.stringify(this.id))
            } else {
              localStorage.removeItem('order-id');
              localStorage.setItem('order-id', JSON.stringify(this.id));
            }
            this.cart.emptyCart();
            window.location.reload();
          },
          err => console.log(err)
        )
      },
      (err) => {
          console.log(err);
      }
  );
  }

}
