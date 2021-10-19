import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { ProductsService } from './../../../services/products.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-lanches-screen',
  templateUrl: './lanches-screen.component.html',
  styleUrls: ['./lanches-screen.component.scss']
})
export class LanchesScreenComponent implements OnInit {

  constructor(private _products : ProductsService, private _auth: AuthService, private _router: Router) { }

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
                    this.lanches = this.products.filter((item)=>item.category==2)
                },
                (response) => {
                    console.log(response);
                }
            );
  }

  navigate(to: string) : void {
    this._router.navigateByUrl(to);
  }

  products: any[] = [];
  lanches: any[] = [];
  admin = false;
}
