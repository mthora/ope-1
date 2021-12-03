import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { ProductsService } from './../../../services/products.service';
import { Component, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser'

@Component({
  selector: 'app-bebidas_sobremesas-screen',
  templateUrl: './bebidas_sobremesas-screen.component.html',
  styleUrls: ['./bebidas_sobremesas-screen.component.scss']
})
export class Bebidas_SobremesasScreenComponent implements OnInit {

  constructor(private _products: ProductsService, private domSanitizer: DomSanitizer,
    private _auth: AuthService, private _router: Router) { }

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
                    this.products = response.data;
                    this.bebidas_sobremesas = this.products.filter((item)=>item.category==3 && item.amount > 0)
                    this.loading = false;
                },
                (response) => {
                    console.log(response);
                }
            );
  }

  navigate(to: string) : void {
    this._router.navigateByUrl(to);
  }

 decodeImg(dataURI: string) {
   let imageblob = atob(btoa(dataURI));
   let image = this.domSanitizer.bypassSecurityTrustUrl(`data:image/png;base64, ${imageblob}`);
   console.log('i', image)
   return image
  }

  admin = false;
  products: any[] = [];
  loading = true;
  bebidas_sobremesas: any[] = [];
}
