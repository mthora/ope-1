import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { ProductsService } from './../../../services/products.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-plates-screen',
  templateUrl: './plates-screen.component.html',
  styleUrls: ['./plates-screen.component.scss']
})
export class PlatesScreenComponent implements OnInit {

  constructor(private _products: ProductsService, private _auth: AuthService, private _router: Router) { }

  ngOnInit() {
    this.getProducts();
    let user = this._auth.getUserId();
    let userRole = user['role'];
    this.admin = userRole == 1;
  }

  getProducts() : any {
    this._products.getProducts()
            .subscribe(
                (response) => {
                    console.log(response);
                    this.products = response.data;
                    this.plates = this.products.filter((item)=>item.category==1 && item.amount > 0)
                },
                (response) => {
                    console.log(response);
                }
            );
  }

  navigate(to: string) : void {
    this._router.navigateByUrl(to);
  }

  admin = false;
  products: any[] = [];
  plates: any[] = [];
}
