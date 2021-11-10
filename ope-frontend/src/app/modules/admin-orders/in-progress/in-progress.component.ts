import { Router } from '@angular/router';
import { OrderService } from './../../../services/order.service';
import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-in-progress',
  templateUrl: './in-progress.component.html',
  styleUrls: ['./in-progress.component.scss']
})
export class InProgressComponent implements OnInit {

  constructor(private _order: OrderService, private _auth: AuthService, private _router: Router) { }

  ngOnInit(): void {
    if (this._auth.getUserId()['role'] != 1) {
      this._router.navigateByUrl('meus-pedidos');
    }
    this.getOrderList();
    console.log(this.filteredOrderList)
  }

  allOrderList: any;
  filteredOrderList: any = null;

  getOrderList(){
    this._order.listOrders().subscribe(
      (res)=>{
        console.log(res);
        this.allOrderList = res.data;
        this.filteredOrderList = this.allOrderList.filter((order: any)=>{
          return (order.done == false || order.done == 0);
        })
      },
      (err)=>{
        console.log(err);
        this.filteredOrderList = null;
      }
    )
  }

}
