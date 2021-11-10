import { Component, OnInit } from '@angular/core';
import { ProductOrderService } from 'src/app/services/product-order.service';

@Component({
  selector: 'app-my-orders',
  templateUrl: './my-orders.component.html',
  styleUrls: ['./my-orders.component.scss']
})
export class MyOrdersComponent implements OnInit {

  constructor(private _productOrder: ProductOrderService) { }

  order: string | null = null;
  orderList : any;
  total: number = 0;

  ngOnInit(): void {
    this.order = localStorage.getItem('order-id');
    if (this.order != null){
      this.getOrderList(parseInt(this.order))
    }
  }

  getOrderList(id: number){
    this._productOrder.getProductOrders(id).subscribe(
      (res)=>{
        this.orderList = res.data
        console.log(this.orderList)
        let value = 0;
        for (let i of this.orderList){
          value+=i.price*(i.amount)
        }
        this.total = parseFloat((value+(value*0.10)).toFixed(2));
      },
      (err)=>{
        this.orderList = null;
        console.log(err);
      }
    )
  }

}
