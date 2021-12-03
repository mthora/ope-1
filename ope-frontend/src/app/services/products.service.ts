import { AuthService } from 'src/app/services/auth.service';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProductsService {
  private _urlProducts: string = `${environment.urlServer}products/`
  constructor(private _httpClient: HttpClient, private _auth: AuthService) { }

  createProduct(form : any) : Observable<any> {
    return this._httpClient.post(this._urlProducts, form, {headers: new HttpHeaders()
      .set('Authorization', `${this._auth.accessToken}`)})
      .pipe(
        switchMap((response: any) => {
            console.log(response);
            return of(response.data);
        })
    );
  }

  deleteProduct(id: number) : Observable<any> {
    return this._httpClient.delete(`${this._urlProducts}${id}`)
      .pipe(
        switchMap((response)=>{
          return of(response);
        })
      )
  }

  uploadImage(file: any, product_id: number) : Observable<any> {
    let formData: FormData = new FormData();
    formData.append('files', file)
    console.log("formData",formData);
    return this._httpClient.post(`${this._urlProducts}img/${product_id}`, formData, {headers: new HttpHeaders()
      .set('Authorization', `${this._auth.accessToken}`)})
      .pipe(
        switchMap((response: any) => {
            console.log(response);
            return of(response.data);
        })
    );
  }

  getImage(product_id: number): Observable<any> {
    return this._httpClient.get(`${this._urlProducts}img/${product_id}`, {responseType: 'text'})
      .pipe(
        switchMap((response)=>{
          return of(response);
        })
      )
  }

  getProducts(): Observable<any> {
    return this._httpClient.get(this._urlProducts, {headers: new HttpHeaders()
      .set('Authorization', `Bearer ${this._auth.accessToken}`)})
      .pipe(
        switchMap((response: any) => {
            console.log(response);
            return of(response);
        })
    );
  }
}
