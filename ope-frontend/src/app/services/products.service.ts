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
